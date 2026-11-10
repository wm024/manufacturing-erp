
{
    "name": "Astrea MRP Management",
    "version": "19.0.1.0.0",
    "summary": "Manufacturing Production Review Management",
    "description": """
        Manufacturing management extension for Astra Manufacturing.
        Includes production review and approval workflows.
    """,
    "category": "Manufacturing",
    "author": "Muhammad Ridho Ramadhan",
    "license": "LGPL-3",
    "depends": [
        "mrp",
        "stock",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "views/production_review_views.xml",
        "views/production_review_menus.xml",
    ],
    "installable": True,
    "application": True,
}
