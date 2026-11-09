# 02 — Master Data and Bill of Materials Specification

**Project:** Astrea Manufacturing — Manufacturing & Production Management ERP  
**ERP Platform:** Odoo 19  
**Document Type:** Master Data Specification  
**Status:** Draft  
**Version:** 1.0

---

# 1. Purpose and Scope

This document defines the master data required to configure and operate the manufacturing processes of Astrea Manufacturing in Odoo 19.

It establishes standardized definitions for:

- Finished products and manufactured subassemblies.
- Raw materials and components.
- Product categories.
- Units of Measure (UoM).
- Bill of Materials (BoM).
- Manufacturing routing and work center operations.
- Manufacturing cost assumptions.
- Master data ownership and governance.

The objective is to establish consistent, accurate, and traceable manufacturing data before production transactions begin.

## 1.1 Scope

The initial implementation covers two primary products:

| Product Code | Product Name | Product Type |
|---|---|---|
| WP100 | Industrial Water Pump | Finished Product |
| EM200 | Industrial Electric Motor | Finished Product / Manufactured Subassembly |

The WP100 Industrial Water Pump uses one EM200 Industrial Electric Motor as a component.

This creates a multi-level manufacturing structure:

```text
WP100 - Industrial Water Pump
│
├── EM200 - Industrial Electric Motor
│   ├── Stator Assembly
│   ├── Rotor Assembly
│   ├── Motor Frame
│   ├── End Shields
│   ├── Bearings
│   ├── Cooling Fan
│   ├── Terminal Box
│   └── Other Components
│
├── Pump Casing
├── Impeller
├── Pump Shaft
├── Mechanical Seal
├── Bearings
├── Coupling
├── Gasket Set
└── Fastener Set
```

**Important:** The product specifications, quantities, and costs in this document are illustrative assumptions for the portfolio project. They must not be interpreted as validated engineering specifications or actual supplier quotations.

---

# 2. Product List

## 2.1 Product Master Data

The following products are included in the initial manufacturing scope.

| Product Code | Product Name | Product Type | Manufacturing Policy | UoM |
|---|---|---|---|---|
| WP100 | Industrial Water Pump | Finished Product | Manufacture | Units |
| EM200 | Industrial Electric Motor | Finished Product / Subassembly | Manufacture | Units |

### Product WP100 — Industrial Water Pump

| Attribute | Value |
|---|---|
| Internal Reference | WP100 |
| Product Name | Industrial Water Pump |
| Product Type | Goods |
| Product Category | Finished Products |
| Unit of Measure | Units |
| Purchase UoM | Units |
| Manufacturing Policy | Manufacture |
| Tracking | By Lot |
| Sales Availability | Yes |
| Purchase Availability | No |
| Routes | Manufacture |
| Responsible Department | Production |
| Product Description | Industrial water pump assembled with an electric motor and mechanical pumping components. |

**Product specification assumptions:**

- Product type: Centrifugal water pump.
- Application: Industrial water circulation.
- Pump casing material: Cast iron.
- Impeller material: Cast iron or engineering-grade equivalent.
- Drive system: EM200 electric motor.
- Production strategy: Make to Stock (MTS) for standard demand, with Make to Order (MTO) as a future extension.
- Quality inspection: Required before finished goods are released.

### Product EM200 — Industrial Electric Motor

| Attribute | Value |
|---|---|
| Internal Reference | EM200 |
| Product Name | Industrial Electric Motor |
| Product Type | Goods |
| Product Category | Manufactured Subassemblies |
| Unit of Measure | Units |
| Purchase UoM | Units |
| Manufacturing Policy | Manufacture |
| Tracking | By Lot |
| Sales Availability | Yes |
| Purchase Availability | No |
| Routes | Manufacture |
| Responsible Department | Production |
| Product Description | Industrial electric motor designed to drive compatible industrial equipment, including WP100. |

**Product specification assumptions:**

- Motor type: Three-phase induction motor.
- Nominal power: 2.2 kW.
- Cooling: Fan-cooled.
- Housing: Industrial metal frame.
- Bearings: Standard industrial rolling bearings.
- Production strategy: Manufactured internally.
- Quality inspection: Required before release to finished goods.

The compatibility between WP100 and EM200 is assumed for this project and must be validated in a real engineering environment.

## 2.2 Product Configuration in Odoo

For both products, configure the following fields in the Odoo product form:

| Odoo Field | Configuration |
|---|---|
| Product Name | Product's official name |
| Internal Reference | Unique product code |
| Product Type | Goods |
| Product Category | According to product classification |
| Unit of Measure | Units |
| Purchase UoM | Units |
| Sales | Enabled |
| Purchase | Disabled for internally manufactured products |
| Inventory Tracking | By Lots |
| Routes | Manufacture |
| Costing Method | Standard Price for the initial costing baseline |
| Inventory Valuation | According to the selected accounting configuration |

**Configuration note:** Odoo 19's available product fields and inventory valuation options depend on installed applications and edition. Verify the actual fields in the installed database before treating this specification as a technical configuration checklist.

---

# 3. Component List

## 3.1 Component Classification

Components are classified into the following groups:

| Category | Description |
|---|---|
| Raw Materials | Materials consumed during manufacturing |
| Purchased Components | Components purchased from external suppliers |
| Manufactured Subassemblies | Components manufactured internally |
| Consumables | Production materials consumed during operations |
| Packaging Materials | Materials used to package finished products |

## 3.2 Component Master Data

The following table defines the initial component catalog.

### A. WP100 Components

| Component Code | Component Name | Category | UoM | Supply Method |
|---|---|---|---|---|
| CMP-PMP-001 | Pump Casing | Purchased Components | Units | Buy |
| CMP-PMP-002 | Impeller | Purchased Components | Units | Buy |
| CMP-PMP-003 | Pump Shaft | Purchased Components | Units | Buy |
| CMP-PMP-004 | Mechanical Seal | Purchased Components | Units | Buy |
| CMP-PMP-005 | Pump Bearing 6205 | Purchased Components | Units | Buy |
| CMP-PMP-006 | Flexible Coupling | Purchased Components | Units | Buy |
| CMP-PMP-007 | Pump Gasket Set | Purchased Components | Sets | Buy |
| CMP-PMP-008 | Pump Fastener Set | Purchased Components | Sets | Buy |
| CMP-PMP-009 | Pump Paint | Consumables | Liters | Buy |
| CMP-PMP-010 | Pump Packaging Set | Packaging Materials | Sets | Buy |

EM200 is also a component of WP100 but is classified as a manufactured subassembly rather than a purchased component.

### B. EM200 Components

| Component Code | Component Name | Category | UoM | Supply Method |
|---|---|---|---|---|
| CMP-MTR-001 | Motor Frame | Purchased Components | Units | Buy |
| CMP-MTR-002 | Stator Assembly | Purchased Components | Units | Buy |
| CMP-MTR-003 | Rotor Assembly | Purchased Components | Units | Buy |
| CMP-MTR-004 | Front End Shield | Purchased Components | Units | Buy |
| CMP-MTR-005 | Rear End Shield | Purchased Components | Units | Buy |
| CMP-MTR-006 | Motor Bearing 6206 | Purchased Components | Units | Buy |
| CMP-MTR-007 | Cooling Fan | Purchased Components | Units | Buy |
| CMP-MTR-008 | Fan Cover | Purchased Components | Units | Buy |
| CMP-MTR-009 | Terminal Box | Purchased Components | Units | Buy |
| CMP-MTR-010 | Terminal Block | Purchased Components | Units | Buy |
| CMP-MTR-011 | Motor Fastener Set | Purchased Components | Sets | Buy |
| CMP-MTR-012 | Motor Insulation Kit | Purchased Components | Sets | Buy |
| CMP-MTR-013 | Motor Paint | Consumables | Liters | Buy |
| CMP-MTR-014 | Motor Packaging Set | Packaging Materials | Sets | Buy |

## 3.3 Component Master Data Rules

Every component must have:

1. A unique internal reference.
2. A standardized product name.
3. An assigned product category.
4. A defined inventory UoM.
5. A defined purchase UoM.
6. A supply method.
7. A defined cost.
8. An assigned supplier, where applicable.
9. A tracking policy, where necessary.
10. An active or inactive status.

### Component Procurement Rules

| Rule ID | Rule |
|---|---|
| CMP-R001 | Purchased components must use the Buy route. |
| CMP-R002 | Manufactured subassemblies must use the Manufacture route. |
| CMP-R003 | Every purchased component must have an approved supplier before procurement. |
| CMP-R004 | Components must use consistent UoM definitions. |
| CMP-R005 | Components with traceability requirements must be tracked by lot or serial number. |
| CMP-R006 | Obsolete components must be archived rather than reused under a different description. |
| CMP-R007 | Component cost changes must follow the approved purchasing or costing process. |

**Important:** Do not enable both Buy and Manufacture routes indiscriminately. A component's supply strategy must reflect its actual procurement and production policy.

---

# 4. Product Categories

## 4.1 Category Structure

Astrea Manufacturing will use a hierarchical product category structure to support inventory classification, reporting, costing, and accounting configuration.

```text
All
│
├── Raw Materials
│
├── Purchased Components
│   ├── Pump Components
│   └── Motor Components
│
├── Manufactured Subassemblies
│
├── Finished Products
│
├── Consumables
│
└── Packaging Materials
```

## 4.2 Category Definition

| Category | Purpose | Example Products |
|---|---|---|
| Raw Materials | Materials used in production | Steel, aluminum, copper wire |
| Purchased Components | Ready-to-use components purchased from suppliers | Pump casing, bearings, impeller |
| Manufactured Subassemblies | Internally manufactured intermediate products | EM200 |
| Finished Products | Products ready for sale | WP100 |
| Consumables | Materials consumed during production | Paint, lubricants |
| Packaging Materials | Materials used for final packaging | Packaging sets |

## 4.3 Category Configuration

Each category should have:

| Attribute | Description |
|---|---|
| Category Name | Standardized category name |
| Parent Category | Parent in the hierarchy |
| Costing Method | Standard Price for initial baseline |
| Inventory Valuation | Configured according to accounting policy |
| Income Account | Relevant sales income account, where applicable |
| Expense Account | Relevant expense account |
| Stock Valuation Account | Relevant inventory valuation account |
| Stock Input Account | Relevant stock input account |
| Stock Output Account | Relevant stock output account |

Accounting accounts must be finalized with the Finance Department.

**Best practice:** Avoid creating a separate product category for every individual product. Categories should represent meaningful accounting or inventory classifications, not merely duplicate product names.

---

# 5. Units of Measure (UoM)

## 5.1 UoM Standardization

Astrea Manufacturing will use standardized Units of Measure to maintain consistency across purchasing, inventory, manufacturing, and costing.

| UoM | Category | Usage |
|---|---|---|
| Units | Unit | Finished products and individual components |
| Sets | Unit | Components supplied as complete sets |
| Kilograms | Weight | Bulk raw materials |
| Grams | Weight | Small material quantities |
| Liters | Volume | Paint and liquid consumables |
| Milliliters | Volume | Small liquid quantities |
| Meters | Length | Wire, cable, and linear materials |
| Millimeters | Length | Engineering measurements, where applicable |

## 5.2 UoM Conversion Rules

UoM conversion must only occur within the same UoM category.

Examples:

| Reference UoM | Alternative UoM | Conversion |
|---|---|---|
| Kilograms | Grams | 1 kg = 1,000 g |
| Liters | Milliliters | 1 L = 1,000 ml |
| Meters | Millimeters | 1 m = 1,000 mm |

For components purchased in boxes or packs, define an appropriate purchase UoM only if the packaging quantity is fixed and documented.

Example:

- Inventory UoM: Units
- Purchase UoM: Units
- Supplier packaging: 10 units per box

Do not assume that one box equals a fixed quantity unless the supplier's packaging specification confirms it.

## 5.3 UoM Configuration Rules

| Rule ID | Rule |
|---|---|
| UOM-R001 | Every product must have a defined inventory UoM. |
| UOM-R002 | Purchase UoM must be compatible with the inventory UoM category. |
| UOM-R003 | UoM conversions must be mathematically accurate. |
| UOM-R004 | UoM changes must be reviewed before production transactions exist. |
| UOM-R005 | UoM names and abbreviations must follow company conventions. |
| UOM-R006 | BoM quantities must use the product's compatible UoM category. |

**Odoo note:** Configure UoM categories and conversion factors through the Units of Measure configuration. Enable the relevant UoM functionality in Inventory settings if it is not already active.

---

# 6. Bill of Materials (BoM) Structure

## 6.1 BoM Design Principles

The Bill of Materials defines the components and quantities required to manufacture a product.

Astrea Manufacturing will use a multi-level BoM structure.

The initial design consists of:

- Level 1: WP100 Industrial Water Pump.
- Level 2: EM200 Industrial Electric Motor.
- Level 3: Components required to manufacture EM200.
- Level 2 components: Pump components required to assemble WP100.

This design enables independent production, inventory tracking, costing, and quality control of EM200.

## 6.2 BoM — WP100 Industrial Water Pump

| Attribute | Value |
|---|---|
| BoM Reference | BOM-WP100-001 |
| Product | WP100 Industrial Water Pump |
| BoM Type | Manufacture this Product |
| Quantity | 1 Unit |
| Version | 1.0 |
| Status | Approved for Project Simulation |

### Component Requirements

| Component | Quantity | UoM |
|---|---:|---|
| EM200 Industrial Electric Motor | 1 | Units |
| Pump Casing | 1 | Units |
| Impeller | 1 | Units |
| Pump Shaft | 1 | Units |
| Mechanical Seal | 1 | Units |
| Pump Bearing 6205 | 2 | Units |
| Flexible Coupling | 1 | Units |
| Pump Gasket Set | 1 | Sets |
| Pump Fastener Set | 1 | Sets |
| Pump Paint | 0.25 | Liters |
| Pump Packaging Set | 1 | Sets |

**Expected production output:** 1 WP100 Industrial Water Pump.

## 6.3 BoM — EM200 Industrial Electric Motor

| Attribute | Value |
|---|---|
| BoM Reference | BOM-EM200-001 |
| Product | EM200 Industrial Electric Motor |
| BoM Type | Manufacture this Product |
| Quantity | 1 Unit |
| Version | 1.0 |
| Status | Approved for Project Simulation |

### Component Requirements

| Component | Quantity | UoM |
|---|---:|---|
| Motor Frame | 1 | Units |
| Stator Assembly | 1 | Units |
| Rotor Assembly | 1 | Units |
| Front End Shield | 1 | Units |
| Rear End Shield | 1 | Units |
| Motor Bearing 6206 | 2 | Units |
| Cooling Fan | 1 | Units |
| Fan Cover | 1 | Units |
| Terminal Box | 1 | Units |
| Terminal Block | 1 | Units |
| Motor Fastener Set | 1 | Sets |
| Motor Insulation Kit | 1 | Sets |
| Motor Paint | 0.20 | Liters |
| Motor Packaging Set | 1 | Sets |

**Expected production output:** 1 EM200 Industrial Electric Motor.

## 6.4 Multi-Level BoM Relationship

```text
WP100 - Industrial Water Pump
│
├── EM200 - Industrial Electric Motor
│   │
│   ├── Motor Frame
│   ├── Stator Assembly
│   ├── Rotor Assembly
│   ├── Front End Shield
│   ├── Rear End Shield
│   ├── Motor Bearing 6206 (2)
│   ├── Cooling Fan
│   ├── Fan Cover
│   ├── Terminal Box
│   ├── Terminal Block
│   ├── Motor Fastener Set
│   ├── Motor Insulation Kit
│   ├── Motor Paint
│   └── Motor Packaging Set
│
├── Pump Casing
├── Impeller
├── Pump Shaft
├── Mechanical Seal
├── Pump Bearing 6205 (2)
├── Flexible Coupling
├── Pump Gasket Set
├── Pump Fastener Set
├── Pump Paint
└── Pump Packaging Set
```

## 6.5 BoM Configuration in Odoo

Navigate to:

**Manufacturing → Products → Bills of Materials**

Create one BoM for each manufactured product.

For WP100:

- Product: WP100 Industrial Water Pump.
- Quantity: 1.
- BoM Type: Manufacture this Product.
- Components: Add all WP100 components, including EM200.
- Operations: Assign WP100 routing operations.

For EM200:

- Product: EM200 Industrial Electric Motor.
- Quantity: 1.
- BoM Type: Manufacture this Product.
- Components: Add all EM200 components.
- Operations: Assign EM200 routing operations.

### BoM Management Rules

| Rule ID | Rule |
|---|---|
| BOM-R001 | Every manufactured product must have an approved BoM. |
| BOM-R002 | Every BoM must have a defined output quantity. |
| BOM-R003 | Every BoM component must reference an active product. |
| BOM-R004 | Component quantities must be reviewed by Engineering. |
| BOM-R005 | Every BoM must have a responsible owner. |
| BOM-R006 | Changes to approved BoMs must follow change control. |
| BOM-R007 | Historical BoM versions must remain traceable. |
| BOM-R008 | A product must not have ambiguous active BoM definitions for the same manufacturing purpose. |
| BOM-R009 | BoM components must use compatible UoMs. |
| BOM-R010 | BoM quantities must reflect the actual manufacturing specification. |

**Important:** Odoo's standard BoM behavior and version management capabilities should be validated against the installed Odoo 19 configuration. Formal engineering revision control may require an additional approval procedure or customization.

---

# 7. Routing and Manufacturing Operations

## 7.1 Routing Overview

Routing defines the sequence of operations required to manufacture a product.

Each operation is assigned to a Work Center.

Astrea Manufacturing will initially use four work centers:

| Work Center Code | Work Center Name | Department |
|---|---|---|
| WC-MCH | Machining | Production |
| WC-FAB | Fabrication | Production |
| WC-ASM | Assembly | Production |
| WC-TST | Testing | Quality / Production |

Work center capacity, working hours, efficiency, setup time, and cost per hour must be configured based on the operational assumptions documented in this project.

## 7.2 Routing — EM200 Industrial Electric Motor

| Sequence | Operation | Work Center | Expected Duration |
|---:|---|---|---:|
| 10 | Prepare Motor Components | Fabrication | 20 minutes |
| 20 | Assemble Stator and Rotor | Assembly | 35 minutes |
| 30 | Install Bearings and End Shields | Assembly | 25 minutes |
| 40 | Install Cooling and Electrical Components | Assembly | 20 minutes |
| 50 | Final Motor Testing | Testing | 20 minutes |

**Total planned operation duration:** 120 minutes per EM200 unit.

These durations are initial planning assumptions, not validated standard times.

## 7.3 Routing — WP100 Industrial Water Pump

| Sequence | Operation | Work Center | Expected Duration |
|---:|---|---|---:|
| 10 | Prepare Pump Components | Fabrication | 20 minutes |
| 20 | Prepare Shaft and Mechanical Components | Machining | 30 minutes |
| 30 | Assemble Pump Components | Assembly | 35 minutes |
| 40 | Install EM200 Motor and Coupling | Assembly | 25 minutes |
| 50 | Perform Final Pump Testing | Testing | 30 minutes |

**Total planned operation duration:** 140 minutes per WP100 unit.

## 7.4 Work Center Configuration

Each work center should have the following master data:

| Attribute | Description |
|---|---|
| Work Center Name | Standard work center name |
| Work Center Code | Unique identifier |
| Capacity | Number of units that can be processed simultaneously |
| Time Efficiency | Estimated work center efficiency |
| OEE Target | Target operational effectiveness |
| Working Hours | Available working schedule |
| Setup Time | Time required to prepare the work center |
| Cleanup Time | Time required after an operation |
| Cost per Hour | Work center hourly operating cost |
| Alternative Work Centers | Approved alternative work centers, if applicable |

### Initial Work Center Assumptions

| Work Center | Capacity | Efficiency | Cost per Hour |
|---|---:|---:|---:|
| Machining | 1 | 90% | $15 |
| Fabrication | 1 | 90% | $12 |
| Assembly | 2 | 95% | $10 |
| Testing | 1 | 90% | $18 |

These values are illustrative and will be used for project simulations.

## 7.5 Routing Rules

| Rule ID | Rule |
|---|---|
| ROUTE-R001 | Every manufacturing operation must have a defined sequence. |
| ROUTE-R002 | Every operation must be assigned to a valid work center. |
| ROUTE-R003 | Operation durations must be defined. |
| ROUTE-R004 | Work centers must be active and available. |
| ROUTE-R005 | Operation sequences must follow the approved production process. |
| ROUTE-R006 | Quality-related operations must include documented inspection criteria. |
| ROUTE-R007 | Routing changes must be approved by Production Engineering. |
| ROUTE-R008 | Work center capacity must reflect actual operational constraints. |

## 7.6 Odoo Configuration

Navigate to:

**Manufacturing → Configuration → Settings**

Enable Work Orders functionality.

Then:

1. Create the four work centers.
2. Configure capacity and operating schedules.
3. Configure work center costs.
4. Open each product's BoM.
5. Add the required manufacturing operations.
6. Assign each operation to the appropriate work center.
7. Configure operation duration.
8. Save and validate the BoM.

The Work Center field in BoM Operations depends on the Manufacturing configuration and valid work center records.

---

# 8. Cost Assumptions

## 8.1 Costing Methodology

The project will use an initial standard cost baseline to simplify costing analysis and manufacturing validation.

Manufacturing cost is divided into:

1. Direct material cost.
2. Direct labor cost.
3. Machine and work center operating cost.
4. Manufacturing overhead.
5. Packaging cost.

The cost model must distinguish between planned cost and actual production cost.

## 8.2 Component Cost Assumptions

The following values are hypothetical supplier or internal standard costs.

### WP100 Components

| Component | Quantity | Unit Cost | Total Cost |
|---|---:|---:|---:|
| EM200 Industrial Electric Motor | 1 | $180.00 | $180.00 |
| Pump Casing | 1 | $45.00 | $45.00 |
| Impeller | 1 | $22.00 | $22.00 |
| Pump Shaft | 1 | $18.00 | $18.00 |
| Mechanical Seal | 1 | $12.00 | $12.00 |
| Pump Bearing 6205 | 2 | $8.00 | $16.00 |
| Flexible Coupling | 1 | $15.00 | $15.00 |
| Pump Gasket Set | 1 | $5.00 | $5.00 |
| Pump Fastener Set | 1 | $4.00 | $4.00 |
| Pump Paint | 0.25 L | $12.00/L | $3.00 |
| Pump Packaging Set | 1 | $8.00 | $8.00 |
| **Total** | | | **$328.00** |

### EM200 Components

| Component | Quantity | Unit Cost | Total Cost |
|---|---:|---:|---:|
| Motor Frame | 1 | $25.00 | $25.00 |
| Stator Assembly | 1 | $35.00 | $35.00 |
| Rotor Assembly | 1 | $30.00 | $30.00 |
| Front End Shield | 1 | $8.00 | $8.00 |
| Rear End Shield | 1 | $8.00 | $8.00 |
| Motor Bearing 6206 | 2 | $7.00 | $14.00 |
| Cooling Fan | 1 | $5.00 | $5.00 |
| Fan Cover | 1 | $6.00 | $6.00 |
| Terminal Box | 1 | $7.00 | $7.00 |
| Terminal Block | 1 | $4.00 | $4.00 |
| Motor Fastener Set | 1 | $3.00 | $3.00 |
| Motor Insulation Kit | 1 | $6.00 | $6.00 |
| Motor Paint | 0.20 L | $10.00/L | $2.00 |
| Motor Packaging Set | 1 | $6.00 | $6.00 |
| **Total** | | | **$159.00** |

## 8.3 Direct Labor Cost Assumptions

For the initial simulation, direct labor is calculated using an assumed labor rate of $8 per hour.

| Product | Total Operation Time | Labor Rate | Direct Labor Cost |
|---|---:|---:|---:|
| EM200 | 120 minutes | $8/hour | $16.00 |
| WP100 | 140 minutes | $8/hour | $18.67 |

Calculation:

```text
Direct Labor Cost =
(Operation Duration in Minutes / 60)
× Labor Rate per Hour
```

The calculation assumes that the listed operation durations represent labor time for one unit and that labor is incurred independently of the work center hourly cost.

If multiple employees work simultaneously, labor cost must be calculated using the actual number of workers assigned to each operation.

## 8.4 Work Center Cost Assumptions

Work center cost is calculated separately from direct labor.

| Product | Work Center | Duration | Hourly Cost | Total |
|---|---|---:|---:|---:|
| EM200 | Fabrication | 20 min | $12 | $4.00 |
| EM200 | Assembly | 80 min | $10 | $13.33 |
| EM200 | Testing | 20 min | $18 | $6.00 |
| **EM200 Total** | | **120 min** | | **$23.33** |
| WP100 | Fabrication | 20 min | $12 | $4.00 |
| WP100 | Machining | 30 min | $15 | $7.50 |
| WP100 | Assembly | 60 min | $10 | $10.00 |
| WP100 | Testing | 30 min | $18 | $9.00 |
| **WP100 Total** | | **140 min** | | **$30.50** |

**Costing note:** This model treats direct labor and work center operating cost as separate cost elements. The work center cost should therefore exclude the labor component to avoid double-counting.

## 8.5 Manufacturing Overhead

For the initial project simulation, manufacturing overhead is assumed to be 10% of direct material cost.

```text
Manufacturing Overhead =
Direct Material Cost × 10%
```

The overhead percentage is a simplified planning assumption. A real manufacturing environment may allocate overhead based on machine hours, labor hours, production volume, or another approved cost driver.

## 8.6 Estimated Manufacturing Cost

### EM200 Cost Calculation

| Cost Component | Amount |
|---|---:|
| Direct Material Cost | $159.00 |
| Direct Labor Cost | $16.00 |
| Work Center Cost | $23.33 |
| Manufacturing Overhead (10% of Material) | $15.90 |
| **Estimated Manufacturing Cost** | **$214.23** |

### WP100 Cost Calculation

WP100 includes one manufactured EM200.

| Cost Component | Amount |
|---|---:|
| EM200 Subassembly Cost | $214.23 |
| Other WP100 Direct Materials | $148.00 |
| Direct Labor Cost | $18.67 |
| Work Center Cost | $30.50 |
| Manufacturing Overhead (10% of Total Direct Material Cost) | $32.80 |
| **Estimated Manufacturing Cost** | **$444.20** |

The WP100 calculation uses the complete EM200 manufacturing cost, including its material, labor, work center, and overhead costs. The $180 EM200 purchase-equivalent component cost must not be added again.

## 8.7 Costing Summary

| Product | Estimated Manufacturing Cost |
|---|---:|
| EM200 Industrial Electric Motor | $214.23 |
| WP100 Industrial Water Pump | $444.20 |

These figures are project planning estimates, not guaranteed Odoo inventory valuation results.

Actual Odoo cost behavior depends on the configured costing method, inventory valuation, accounting setup, work order execution, and installed modules.

### Costing Rules

| Rule ID | Rule |
|---|---|
| COST-R001 | Every purchased component must have an approved cost baseline. |
| COST-R002 | Manufactured products must include their relevant component and production costs. |
| COST-R003 | Subassembly cost must be included in the parent product cost without duplication. |
| COST-R004 | Labor and work center costs must be separated consistently. |
| COST-R005 | Manufacturing overhead must follow an approved allocation basis. |
| COST-R006 | Cost changes must be reviewed and approved by Finance. |
| COST-R007 | Planned costs and actual costs must be distinguishable. |
| COST-R008 | Cost assumptions must be reviewed periodically. |

**Odoo implementation consideration:**

Standard Price, Average Cost (AVCO), and FIFO have different inventory valuation behaviors. Do not assume that entering a BoM and work center cost automatically produces the same result as the estimated costing table above.

For the portfolio project:

- Use Standard Price as the initial baseline.
- Configure product and category valuation consistently.
- Validate the behavior of manufacturing cost updates with test Manufacturing Orders.
- Document any differences between the analytical cost model and Odoo's resulting valuation.

---

# 9. Master Data Ownership

## 9.1 Ownership Principles

Master data ownership ensures that every critical manufacturing record has a responsible department.

No user should be able to modify critical master data without appropriate authorization.

The following departments are responsible for maintaining the accuracy of master data.

## 9.2 Responsibility Matrix

| Master Data | Responsible Department | Approver | Supporting Department |
|---|---|---|---|
| Product Master | Engineering | Engineering Manager | Production |
| Component Master | Procurement | Procurement Manager | Engineering |
| Product Category | Finance | Finance Manager | Inventory |
| UoM | Inventory | Inventory Manager | Engineering |
| Bill of Materials | Engineering | Engineering Manager | Production |
| Routing | Production Engineering | Production Manager | Engineering |
| Work Centers | Production | Production Manager | Maintenance |
| Standard Costs | Finance | Finance Manager | Procurement |
| Supplier Information | Procurement | Procurement Manager | Finance |
| Inventory Tracking Policy | Inventory | Inventory Manager | Quality |
| Quality Inspection Criteria | Quality | Quality Manager | Engineering |

## 9.3 Master Data Responsibilities

### Engineering Department

Responsibilities:

- Define product specifications.
- Create and maintain product master records.
- Define component specifications.
- Create and maintain BoMs.
- Validate component quantities.
- Approve engineering changes.
- Maintain product revisions.

### Procurement Department

Responsibilities:

- Maintain supplier information.
- Define approved supplier relationships.
- Maintain purchasing specifications.
- Validate supplier pricing.
- Review component availability.
- Communicate supplier-related changes.

### Production Department

Responsibilities:

- Define manufacturing routing.
- Maintain work center assignments.
- Validate operation sequences.
- Maintain standard operation durations.
- Report production process changes.
- Validate production feasibility.

### Inventory Department

Responsibilities:

- Maintain inventory UoM.
- Maintain inventory classification.
- Monitor stock accuracy.
- Manage product traceability.
- Validate inventory transactions.
- Maintain warehouse-related product settings.

### Finance Department

Responsibilities:

- Define costing policies.
- Maintain standard cost assumptions.
- Review inventory valuation.
- Validate product category accounting.
- Approve cost changes.
- Review manufacturing cost reports.

### Quality Department

Responsibilities:

- Define quality inspection requirements.
- Maintain quality control specifications.
- Define lot traceability requirements.
- Approve quality-related master data.
- Review product inspection criteria.

## 9.4 Master Data Change Management

All critical master data changes must follow a controlled process.

```text
Change Request
      |
      v
Request Submitted
      |
      v
Responsible Department Review
      |
      v
Technical / Business Validation
      |
      v
Authorized Approval
      |
      v
Master Data Updated in Odoo
      |
      v
Validation and Testing
      |
      v
Change Log Recorded
```

### Change Management Rules

| Rule ID | Rule |
|---|---|
| MD-R001 | Every critical master data change must have a documented reason. |
| MD-R002 | Changes must be approved by the designated owner. |
| MD-R003 | BoM changes must be reviewed by Engineering. |
| MD-R004 | Routing changes must be approved by Production Management. |
| MD-R005 | Cost changes must be approved by Finance. |
| MD-R006 | Changes affecting existing manufacturing orders must be assessed before implementation. |
| MD-R007 | Obsolete master data should be archived when no longer needed. |
| MD-R008 | Historical manufacturing transactions must remain traceable. |
| MD-R009 | Access to critical master data must be restricted by user role. |
| MD-R010 | Master data should be reviewed periodically. |

## 9.5 Master Data Governance in Odoo

The following access principles should be implemented:

| Role | Access |
|---|---|
| Manufacturing User | Read product and BoM data; execute manufacturing transactions |
| Manufacturing Manager | Manage manufacturing configuration and approve production-related changes |
| Inventory User | Maintain permitted inventory product information and inventory operations |
| Inventory Manager | Manage inventory master data and warehouse configuration |
| Purchase User | Manage purchasing transactions and supplier information |
| Purchase Manager | Approve procurement-related changes |
| Finance User | Review cost and accounting data |
| Finance Manager | Approve costing and valuation configuration |
| Quality User | Perform quality inspections |
| Quality Manager | Manage quality control configuration |
| Administrator | Technical configuration and access administration |

Actual access rights must be validated against Odoo's installed modules and standard security groups. Use record rules and custom groups only when standard permissions are insufficient.

---

# 10. Master Data Validation Checklist

Before the first Manufacturing Order is created, validate the following items.

## 10.1 Product Validation

- [ ] WP100 exists in Odoo.
- [ ] EM200 exists in Odoo.
- [ ] Internal references are unique.
- [ ] Product categories are assigned.
- [ ] Inventory UoM is configured.
- [ ] Product routes are configured.
- [ ] Tracking policy is configured.
- [ ] Product descriptions are complete.

## 10.2 Component Validation

- [ ] All WP100 components exist.
- [ ] All EM200 components exist.
- [ ] Component references are unique.
- [ ] Component categories are assigned.
- [ ] UoM is correct.
- [ ] Supply methods are correct.
- [ ] Supplier information is available where required.
- [ ] Standard cost assumptions are documented.

## 10.3 BoM Validation

- [ ] WP100 BoM exists.
- [ ] EM200 BoM exists.
- [ ] BoM output quantity is correct.
- [ ] All required components are assigned.
- [ ] Component quantities are correct.
- [ ] Component UoM is compatible.
- [ ] Multi-level BoM relationship is correct.
- [ ] No duplicate component requirements exist.
- [ ] BoM has been reviewed by Engineering.

## 10.4 Routing Validation

- [ ] Machining work center exists.
- [ ] Fabrication work center exists.
- [ ] Assembly work center exists.
- [ ] Testing work center exists.
- [ ] Work center capacities are configured.
- [ ] Work center operating costs are configured.
- [ ] Operation sequences are correct.
- [ ] Operation durations are configured.
- [ ] Each operation has a valid work center.
- [ ] Work Orders functionality is enabled.

## 10.5 Cost Validation

- [ ] Component costs are documented.
- [ ] Direct labor assumptions are documented.
- [ ] Work center cost assumptions are documented.
- [ ] Manufacturing overhead is defined.
- [ ] Subassembly costing is not double-counted.
- [ ] Product costing configuration is reviewed.
- [ ] Cost calculations are validated using test manufacturing orders.

---

# 11. Acceptance Criteria

The master data configuration is considered complete when:

| ID | Acceptance Criteria |
|---|---|
| MD-AC-001 | All defined products exist in Odoo. |
| MD-AC-002 | All required components exist in Odoo. |
| MD-AC-003 | Product categories follow the approved hierarchy. |
| MD-AC-004 | All products have valid UoM definitions. |
| MD-AC-005 | UoM conversions are accurate. |
| MD-AC-006 | WP100 has an approved BoM. |
| MD-AC-007 | EM200 has an approved BoM. |
| MD-AC-008 | WP100 correctly references EM200 as a manufactured subassembly. |
| MD-AC-009 | All BoM components have valid product references. |
| MD-AC-010 | All manufacturing operations have valid work center assignments. |
| MD-AC-011 | Work center capacity and cost assumptions are configured. |
| MD-AC-012 | Estimated manufacturing costs can be reconciled with the documented cost model. |
| MD-AC-013 | Master data ownership is defined. |
| MD-AC-014 | Master data changes follow an approval process. |
| MD-AC-015 | Master data validation checklist is completed. |

---

# 12. Dependencies and Related Documentation

This document depends on the following project documents:

| Document | Relationship |
|---|---|
| `01_business_requirements.md` | Defines business requirements and manufacturing scope |
| `02_master_data_and_bom.md` | Defines products, components, BoMs, routing, costing, and ownership |
| `03_functional_specification.md` | Defines detailed system behavior and configuration |
| `04_technical_architecture.md` | Defines the technical implementation architecture |
| `05_test_strategy_and_test_cases.md` | Defines test scenarios and validation procedures |

---

# 13. Final Notes

This master data specification establishes the baseline manufacturing structure for Astrea Manufacturing.

The most important implementation principles are:

1. Maintain a clear separation between finished products, manufactured subassemblies, and purchased components.
2. Use multi-level BoMs to represent actual manufacturing dependencies.
3. Keep UoM definitions consistent across purchasing, inventory, and manufacturing.
4. Define routing operations based on real production sequences.
5. Separate direct labor, work center costs, and manufacturing overhead.
6. Establish clear master data ownership and approval responsibilities.
7. Validate all assumptions through test Manufacturing Orders before production deployment.

**Implementation status:** Initial master data design completed. Actual Odoo configuration and validation remain subject to implementation testing.

