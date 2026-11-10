
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class ProductionReview(models.Model):
    _name = "astrea.production.review"
    _description = "Manufacturing Production Review"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "create_date desc, id desc"

    name = fields.Char(
        string="Review Reference",
        required=True,
        copy=False,
        readonly=True,
        default=lambda self: _("New"),
        tracking=True,
    )

    production_id = fields.Many2one(
        comodel_name="mrp.production",
        string="Manufacturing Order",
        required=True,
        ondelete="restrict",
        index=True,
        tracking=True,
    )

    product_id = fields.Many2one(
        related="production_id.product_id",
        string="Product",
        store=True,
        readonly=True,
    )

    product_qty = fields.Float(
        related="production_id.product_qty",
        string="Planned Quantity",
        readonly=True,
    )

    reviewer_id = fields.Many2one(
        comodel_name="res.users",
        string="Reviewer",
        default=lambda self: self.env.user,
        required=True,
        tracking=True,
    )

    review_date = fields.Date(
        string="Review Date",
        default=fields.Date.context_today,
        required=True,
    )

    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("approved", "Approved"),
            ("rejected", "Rejected"),
        ],
        default="draft",
        required=True,
        tracking=True,
    )

    notes = fields.Text(string="Review Notes")

    company_id = fields.Many2one(
        related="production_id.company_id",
        store=True,
        readonly=True,
    )

    _sql_constraints = [
        (
            "production_review_unique",
            "unique(production_id)",
            "A production order can only have one review.",
        ),
    ]

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("name", _("New")) == _("New"):
                vals["name"] = self.env["ir.sequence"].next_by_code(
                    "astrea.production.review"
                ) or _("New")

        return super().create(vals_list)

    def action_approve(self):
        for record in self:
            if record.state != "draft":
                raise UserError(
                    _("Only draft reviews can be approved.")
                )

            if not record.notes:
                raise ValidationError(
                    _("Review notes are required before approval.")
                )

            record.state = "approved"

    def action_reject(self):
        for record in self:
            if record.state != "draft":
                raise UserError(
                    _("Only draft reviews can be rejected.")
                )

            if not record.notes:
                raise ValidationError(
                    _("Rejection reason is required.")
                )

            record.state = "rejected"

    def action_reset_to_draft(self):
        for record in self:
            if record.state not in ("approved", "rejected"):
                raise UserError(
                    _("Only reviewed records can be reset.")
                )

            record.state = "draft"
