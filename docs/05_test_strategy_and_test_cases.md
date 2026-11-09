# 05 — Test Strategy and Test Cases

**Project:** Astra Manufacturing — Manufacturing & Production Management ERP  
**ERP Platform:** Odoo 19  
**Database:** PostgreSQL  
**Document Type:** Software Test Strategy and Test Case Specification  
**Version:** 1.0  
**Status:** Draft — Portfolio Simulation  
**Document Path:** `documentations/05_test_strategy_and_test_cases.md`

---

## 1. Introduction

### 1.1 Purpose

This document defines the testing strategy, test scope, test scenarios, test cases, execution procedures, and acceptance criteria for the Astra Manufacturing ERP implementation project.

The primary objective is to verify that the configured Odoo 19 system supports the required manufacturing and operational processes while maintaining data accuracy, process integrity, security, and system reliability.

This document serves as the primary reference for:

- Functional testing.
- Integration testing.
- End-to-end process testing.
- Regression testing.
- User Acceptance Testing (UAT).
- Technical and security testing.
- Defect management.
- Test execution and reporting.

### 1.2 Project Overview

Astra Manufacturing is a hypothetical manufacturing company used as a portfolio case study.

The proposed ERP implementation focuses on managing manufacturing operations, inventory, procurement, product configuration, quality control, and related financial processes.

The primary products are:

| Product Code | Product Name |
|---|---|
| WP100 | Industrial Water Pump |
| EM200 | Industrial Electric Motor |

The manufacturing process uses the following work centers:

| Work Center | Description |
|---|---|
| Machining | Mechanical component machining |
| Fabrication | Component fabrication |
| Assembly | Product and subassembly assembly |
| Testing | Product inspection and functional testing |

All business data, test records, expected results, and operational scenarios in this document are illustrative. They must be validated against the final business requirements and actual system configuration.

### 1.3 Testing Objectives

The testing process aims to:

1. Verify that implemented functions satisfy approved business requirements.
2. Validate manufacturing workflows from demand creation through production completion.
3. Verify inventory movements and material consumption.
4. Validate Bills of Materials (BoMs), routings, operations, and work center configurations.
5. Verify procurement and replenishment workflows.
6. Validate quality inspection and nonconformance handling.
7. Verify production costing and accounting integration where applicable.
8. Ensure access rights and record-level security are correctly configured.
9. Identify defects before production deployment.
10. Confirm that the system meets the agreed acceptance criteria.

### 1.4 Testing Principles

The project follows these testing principles:

- **Risk-based testing:** Prioritize critical manufacturing and inventory processes.
- **Requirement traceability:** Every test must be connected to a requirement or documented technical control.
- **Repeatability:** Test cases must be reproducible using controlled test data.
- **Independence:** Expected results must be defined before execution.
- **Evidence-based validation:** Test results must be supported by screenshots, logs, reports, or database records where appropriate.
- **Environment separation:** Development, testing, and production environments must remain separate.
- **Regression protection:** Changes must not unintentionally break previously validated workflows.
- **No false sign-off:** A test must not be marked as passed without execution evidence.

---

## 2. Testing Scope

### 2.1 In-Scope Modules

The following Odoo applications and functional areas are included in the proposed test scope.

| Application / Area | Testing Scope |
|---|---|
| Manufacturing | Manufacturing Orders, BoMs, operations, work orders |
| Inventory | Receipts, internal transfers, reservations, consumption, finished goods |
| Purchase | Purchase Orders, vendor receipts, replenishment |
| Quality | Quality control points, checks, quality alerts, nonconformance |
| Maintenance | Equipment records and maintenance workflows, if configured |
| Sales | Sales demand and MTO-related integration, if configured |
| Accounting | Manufacturing-related valuation and accounting integration, depending on configuration |
| Users & Access Rights | User roles, permissions, company access |
| Reporting | Manufacturing, inventory, procurement, and operational reports |
| System Administration | Configuration, backups, logging, deployment controls |

**Implementation note:** The availability and exact behavior of features depend on the installed Odoo applications, edition, configuration, and any custom modules. Verify the actual Odoo 19 installation before finalizing individual test procedures.

### 2.2 Out-of-Scope

The following activities are excluded unless separately approved:

- Testing external applications not integrated with Odoo.
- Full-scale industrial equipment testing.
- Physical machine automation and PLC integration.
- Advanced production scheduling optimization beyond configured Odoo functionality.
- Third-party payment gateway testing.
- Mobile applications outside the supported Odoo interface.
- Penetration testing by an independent security provider.
- Production migration from an actual legacy ERP.
- Regulatory certification or formal industrial compliance audits.

### 2.3 Testing Scope by Business Process

| Business Process | Included |
|---|---|
| Product and component master data | Yes |
| BoM creation and validation | Yes |
| Routing and work center configuration | Yes |
| Procurement and vendor receipt | Yes |
| Inventory replenishment | Yes |
| Manufacturing Order creation | Yes |
| Material reservation | Yes |
| Work order execution | Yes |
| Material consumption | Yes |
| Finished goods production | Yes |
| Quality inspection | Yes |
| Scrap and rework handling | Yes, subject to configuration |
| Manufacturing cost analysis | Yes, subject to costing configuration |
| Accounting integration | Conditional |
| User access control | Yes |
| Backup and restoration | Yes |
| Performance testing | Yes, within agreed test capacity |

---

## 3. Test Strategy

### 3.1 Test Levels

The project uses the following testing levels.

#### 3.1.1 Unit Testing

Unit testing validates individual custom-developed components independently.

Examples:

- Custom model methods.
- Computed fields.
- Constraints.
- Automated actions.
- Custom business logic.
- Custom report calculations.
- Custom API methods.

For custom Odoo modules, automated tests should use the Odoo testing framework where appropriate.

Recommended validation:

- Positive test cases.
- Negative test cases.
- Boundary-value testing.
- Constraint validation.
- Access-right validation.
- Error handling.

**Responsibility:** Developer.

#### 3.1.2 Integration Testing

Integration testing verifies that related Odoo applications exchange data correctly.

Examples:

- Purchase Order to Inventory Receipt.
- Inventory availability to Manufacturing Order reservation.
- Manufacturing Order to Work Orders.
- Work Order completion to material consumption.
- Production completion to finished goods inventory.
- Quality checks to manufacturing workflow.
- Inventory valuation to Accounting, when applicable.

**Responsibility:** Developer and Functional Consultant.

#### 3.1.3 System Testing

System testing validates the complete configured ERP system against the defined functional and non-functional requirements.

Examples:

- Complete manufacturing lifecycle.
- Procurement and replenishment.
- Quality management.
- Inventory accuracy.
- Reporting.
- User permissions.
- System configuration.

**Responsibility:** QA Tester.

#### 3.1.4 User Acceptance Testing (UAT)

UAT validates whether the implemented ERP supports business users' actual operational requirements.

Proposed participants:

| Role | UAT Responsibility |
|---|---|
| Project Sponsor | Business acceptance |
| Production Manager | Manufacturing workflow validation |
| Production Supervisor | Work order execution validation |
| Warehouse Manager | Inventory and material movement validation |
| Procurement Manager | Procurement validation |
| Quality Manager | Quality process validation |
| Finance Manager | Costing and accounting validation |
| IT Administrator | Technical and operational validation |

For this portfolio project, UAT participants are hypothetical roles. Do not represent simulated UAT as an actual stakeholder approval.

**Responsibility:** Business Users / Simulated UAT Participants.

### 3.2 Test Types

| Test Type | Objective |
|---|---|
| Functional Testing | Validate business functions |
| Integration Testing | Validate cross-module interactions |
| Positive Testing | Verify valid business transactions |
| Negative Testing | Verify invalid transactions are rejected or controlled |
| Boundary Testing | Validate minimum, maximum, and threshold values |
| Regression Testing | Detect defects introduced by changes |
| Security Testing | Validate authentication and authorization |
| Performance Testing | Assess response time and throughput |
| Compatibility Testing | Validate supported browsers and environments |
| Backup & Recovery Testing | Validate data restoration procedures |
| User Acceptance Testing | Validate business suitability |

### 3.3 Risk-Based Testing Priorities

| Priority | Description | Example |
|---|---|---|
| P1 — Critical | Failure may stop production or compromise critical data | Incorrect material consumption |
| P2 — High | Failure significantly affects business operations | Incorrect stock reservation |
| P3 — Medium | Failure affects a limited workflow | Incorrect operational report |
| P4 — Low | Minor usability or cosmetic issue | Label alignment |

Testing should prioritize P1 and P2 scenarios before lower-risk scenarios.

### 3.4 Test Execution Order

Recommended execution sequence:

1. Environment readiness validation.
2. Master data validation.
3. Configuration testing.
4. Unit testing.
5. Functional testing.
6. Integration testing.
7. End-to-end testing.
8. Security testing.
9. Performance testing.
10. Regression testing.
11. UAT.
12. Final acceptance review.

---

## 4. Test Environment

### 4.1 Environment Architecture

The project uses separate environments to reduce deployment and testing risks.

| Environment | Purpose | Data |
|---|---|---|
| Development | Customization and development | Synthetic development data |
| Testing / QA | Functional, integration, and regression testing | Controlled test data |
| Staging / UAT | Business validation and release rehearsal | UAT test data |
| Production | Live business operations | Actual business data |

All environments must be installed and managed without Docker for this project.

### 4.2 Proposed Technology Stack

| Component | Technology |
|---|---|
| Operating System | Ubuntu Server LTS |
| ERP | Odoo 19 |
| Programming Language | Python |
| Database | PostgreSQL |
| Web Server | Nginx |
| Process Manager | systemd |
| Source Control | Git |
| Testing Framework | Odoo Test Framework / Python unittest |
| Browser Testing | Manual testing and optional Playwright |
| API Testing | Postman or equivalent |
| Performance Testing | Locust or equivalent |
| Monitoring | Linux logs and selected monitoring tools |

Version compatibility must be verified before execution.

### 4.3 Test Environment Readiness Checklist

| ID | Validation | Expected Condition |
|---|---|---|
| ENV-001 | Odoo installation | Odoo 19 starts successfully |
| ENV-002 | PostgreSQL connection | Database connection succeeds |
| ENV-003 | Required applications | Required modules are installed |
| ENV-004 | Custom addons | Custom modules load successfully |
| ENV-005 | User accounts | Test users are available |
| ENV-006 | Test database | Isolated test database exists |
| ENV-007 | Filestore | Filestore is accessible |
| ENV-008 | Logging | Application logs are available |
| ENV-009 | Backup | Test backup can be generated |
| ENV-010 | Browser | Supported browser can access Odoo |

**Environment readiness gate:** Testing must not begin if critical environment checks fail.

---

## 5. Test Data Management

### 5.1 Test Data Principles

Test data must be:

- Synthetic and clearly identified.
- Consistent across related test cases.
- Reusable where appropriate.
- Isolated from production data.
- Reproducible.
- Resettable between test cycles.
- Representative of normal and exceptional business scenarios.

Do not use real customer, employee, supplier, or financial information in portfolio test environments.

### 5.2 Product Master Data

Illustrative test data:

| Product Code | Product Name | Product Type |
|---|---|---|
| WP100 | Industrial Water Pump | Manufactured |
| EM200 | Industrial Electric Motor | Manufactured |
| CMP001 | Steel Housing | Component |
| CMP002 | Copper Wire | Component |
| CMP003 | Bearing Set | Component |
| CMP004 | Impeller | Component |
| CMP005 | Fastener Set | Component |
| CMP006 | Electrical Control Unit | Component |

The final BoM must be based on the approved engineering design for the hypothetical project.

### 5.3 Work Center Test Data

| Work Center Code | Work Center Name |
|---|---|
| WC001 | Machining |
| WC002 | Fabrication |
| WC003 | Assembly |
| WC004 | Testing |

### 5.4 Inventory Test Data

Illustrative quantities:

| Component | Initial Quantity | Reordering Threshold |
|---|---:|---:|
| CMP001 | 100 Units | 20 Units |
| CMP002 | 150 Meters | 30 Meters |
| CMP003 | 80 Units | 20 Units |
| CMP004 | 60 Units | 15 Units |
| CMP005 | 200 Units | 50 Units |
| CMP006 | 40 Units | 10 Units |

These values are test fixtures, not validated procurement policies.

### 5.5 Test User Accounts

| User ID | Role | Intended Access |
|---|---|---|
| TEST-ADMIN | Administrator | System configuration |
| TEST-MFG-MGR | Manufacturing Manager | Manufacturing management |
| TEST-MFG-USER | Manufacturing User | Assigned manufacturing operations |
| TEST-WH-MGR | Warehouse Manager | Inventory management |
| TEST-PUR-MGR | Purchase Manager | Procurement management |
| TEST-QA-MGR | Quality Manager | Quality management |
| TEST-FIN-MGR | Finance Manager | Accounting access, if configured |

Use separate accounts to validate access rights. Do not conduct security testing exclusively through an administrator account.

### 5.6 Test Data Reset Strategy

Before each major test cycle:

1. Confirm the test database is isolated.
2. Record the database backup or baseline.
3. Reset transactions using an approved cleanup procedure.
4. Recreate required test data.
5. Verify stock quantities and reservations.
6. Verify product and BoM configurations.
7. Record the test data version.

Avoid deleting transactional records directly from PostgreSQL. Use Odoo-supported business operations or restore a clean test database snapshot.

---

## 6. Requirement Traceability

### 6.1 Traceability Objective

Requirement Traceability Matrix (RTM) ensures that approved business requirements are covered by test cases.

Each test case should map to one or more approved requirement IDs.

The project BRD defines requirement identifier ranges:

- Functional Requirements: FR-001 to FR-081.
- Business Rules: BR-001 to BR-048.
- Acceptance Criteria: AC-001 to AC-048.

The exact semantic mapping must be verified against the final approved `01_business_requirements.md`. Do not assign a requirement ID to a test case solely because its number appears relevant.

### 6.2 Requirement Traceability Matrix Template

| Test Case ID | Requirement ID | Business Rule ID | Acceptance Criteria ID | Status |
|---|---|---|---|---|
| TC-MDM-001 | TBD | TBD | TBD | Pending mapping |
| TC-BOM-001 | TBD | TBD | TBD | Pending mapping |
| TC-MFG-001 | TBD | TBD | TBD | Pending mapping |
| TC-INV-001 | TBD | TBD | TBD | Pending mapping |
| TC-PUR-001 | TBD | TBD | TBD | Pending mapping |
| TC-QA-001 | TBD | TBD | TBD | Pending mapping |
| TC-CST-001 | TBD | TBD | TBD | Pending mapping |
| TC-SEC-001 | TBD | TBD | TBD | Pending mapping |

**Important:** The `TBD` entries must be resolved against the final BRD and Functional Specification before the test suite is approved. The test case identifiers in this document are test identifiers, not substitutes for FR or AC identifiers.

### 6.3 Traceability Completion Criteria

The RTM is considered complete when:

- Every in-scope functional requirement has at least one relevant test case.
- Every critical business rule has a corresponding validation.
- Every acceptance criterion has measurable verification evidence.
- All test cases reference valid requirement IDs.
- Uncovered requirements are documented as testing gaps.
- Out-of-scope requirements are explicitly identified.

---

## 7. Functional Test Cases

### 7.1 Master Data Management

#### TC-MDM-001 — Create Manufactured Product

| Attribute | Details |
|---|---|
| Test Case ID | TC-MDM-001 |
| Module | Inventory / Manufacturing |
| Priority | P1 |
| Test Type | Functional |
| Preconditions | User has permission to create products |
| Test Data | WP100 — Industrial Water Pump |

**Test Steps**

1. Open the Products menu.
2. Create a new product.
3. Enter product name and internal reference.
4. Configure the product as a manufactured product according to the installed Odoo 19 configuration.
5. Save the product.
6. Reopen the product record.

**Expected Results**

- Product is created successfully.
- Product name and internal reference are stored correctly.
- Product configuration is consistent with the manufacturing workflow.
- The product can be selected in the relevant manufacturing configuration.

Actual Result: ____________________

Status: Not Executed

Evidence: ____________________

#### TC-MDM-002 — Create Component Product

| Attribute | Details |
|---|---|
| Test Case ID | TC-MDM-002 |
| Module | Inventory |
| Priority | P1 |
| Test Type | Functional |
| Preconditions | User has product creation access |
| Test Data | CMP001 — Steel Housing |

**Test Steps**

1. Open Products.
2. Create CMP001.
3. Configure its product type and unit of measure.
4. Save the record.
5. Reopen the record.

**Expected Results**

- Component product is created successfully.
- Product reference is unique.
- Unit of measure is correctly configured.
- Product can be used as a BoM component.

Actual Result: ____________________

Status: Not Executed

Evidence: ____________________

#### TC-MDM-003 — Prevent Duplicate Internal Reference

| Attribute | Details |
|---|---|
| Test Case ID | TC-MDM-003 |
| Module | Inventory |
| Priority | P2 |
| Test Type | Negative |
| Preconditions | WP100 already exists |
| Test Data | Duplicate internal reference WP100 |

**Test Steps**

1. Create a new product.
2. Enter an internal reference already assigned to WP100.
3. Save the record.

**Expected Results**

- The system prevents duplicate references if uniqueness is part of the approved data policy.
- A clear validation message is displayed or the configured duplicate-control mechanism is triggered.
- Existing product data remains unchanged.

Actual Result: ____________________

Status: Not Executed

Evidence: ____________________

---

### 7.2 Bill of Materials and Routing

#### TC-BOM-001 — Create Bill of Materials

| Attribute | Details |
|---|---|
| Test Case ID | TC-BOM-001 |
| Module | Manufacturing |
| Priority | P1 |
| Test Type | Functional |
| Preconditions | Product and component records exist |
| Test Data | WP100 and approved illustrative component structure |

**Test Steps**

1. Open Manufacturing.
2. Navigate to Products / Bills of Materials.
3. Create a BoM for WP100.
4. Select the appropriate BoM type.
5. Add the required components and quantities.
6. Configure operations if the BoM uses routing.
7. Save the BoM.
8. Reopen the record.

**Expected Results**

- BoM is created successfully.
- Finished product is correctly assigned.
- Component quantities and units of measure are correct.
- Required operations are available.
- No invalid or unintended component references exist.

Actual Result: ____________________

Status: Not Executed

Evidence: ____________________

#### TC-BOM-002 — Validate BoM Component Availability

| Attribute | Details |
|---|---|
| Test Case ID | TC-BOM-002 |
| Module | Manufacturing |
| Priority | P1 |
| Test Type | Functional |
| Preconditions | BoM exists |
| Test Data | WP100 BoM |

**Test Steps**

1. Open the WP100 BoM.
2. Review all components.
3. Verify component quantities.
4. Verify units of measure.
5. Compare the configuration against the approved illustrative engineering specification.

**Expected Results**

- All required components are present.
- Component quantities match the approved specification.
- Units of measure are consistent.
- No unintended duplicate or circular BoM structure exists.

Actual Result: ____________________

Status: Not Executed

Evidence: ____________________

#### TC-BOM-003 — Configure Routing Operations

| Attribute | Details |
|---|---|
| Test Case ID | TC-BOM-003 |
| Module | Manufacturing |
| Priority | P1 |
| Test Type | Functional |
| Preconditions | Work centers exist and work order functionality is enabled |
| Test Data | Machining, Fabrication, Assembly, Testing |

**Test Steps**

1. Open the WP100 BoM.
2. Configure its operations.
3. Assign the appropriate work center to each operation.
4. Set operation sequence and expected duration.
5. Save the BoM.
6. Reopen the routing configuration.

**Expected Results**

- Each operation is saved successfully.
- The assigned work center is valid and selectable.
- Operation sequence is correct.
- The configuration can be used to generate work orders.

Actual Result: ____________________

Status: Not Executed

Evidence: ____________________

#### TC-BOM-004 — Prevent Invalid Routing Configuration

| Attribute | Details |
|---|---|
| Test Case ID | TC-BOM-004 |
| Module | Manufacturing |
| Priority | P2 |
| Test Type | Negative |
| Preconditions | BoM exists |
| Test Data | Invalid or unavailable work center assignment |

**Test Steps**

1. Open the BoM routing configuration.
2. Attempt to assign an unavailable or invalid work center.
3. Save the configuration.

**Expected Results**

- Invalid configuration is rejected or remains unavailable according to the configured Odoo validation.
- No unintended routing record is created.
- Existing valid operations remain unchanged.

Actual Result: ____________________

Status: Not Executed

Evidence: ____________________

---

### 7.3 Procurement and Inventory

#### TC-PUR-001 — Create Purchase Order

| Attribute | Details |
|---|---|
| Test Case ID | TC-PUR-001 |
| Module | Purchase |
| Priority | P1 |
| Test Type | Functional |
| Preconditions | Vendor and component records exist |
| Test Data | CMP001, illustrative vendor, quantity 100 |

**Test Steps**

1. Open Purchase.
2. Create a new RFQ.
3. Select the test vendor.
4. Add CMP001.
5. Enter quantity and illustrative unit price.
6. Confirm the Purchase Order.
7. Reopen the order.

**Expected Results**

- RFQ is created successfully.
- Purchase Order is confirmed successfully.
- Vendor, product, quantity, and price are correct.
- A receipt operation is generated when the configured workflow requires it.

Actual Result: ____________________

Status: Not Executed

Evidence: ____________________

#### TC-PUR-002 — Receive Purchased Components

| Attribute | Details |
|---|---|
| Test Case ID | TC-PUR-002 |
| Module | Purchase / Inventory |
| Priority | P1 |
| Test Type | Integration |
| Preconditions | Confirmed Purchase Order exists |
| Test Data | CMP001 — 100 Units |

**Test Steps**

1. Open the confirmed Purchase Order.
2. Open the associated receipt.
3. Verify the received product and quantity.
4. Validate the receipt.
5. Open the product inventory report.
6. Verify the resulting stock quantity.

**Expected Results**

- Receipt is linked to the correct Purchase Order.
- Received quantity is recorded correctly.
- Inventory is updated according to the configured stock operation.
- The receipt is traceable to its source document.

Actual Result: ____________________

Status: Not Executed

Evidence: ____________________

#### TC-INV-001 — Verify Inventory On Hand

| Attribute | Details |
|---|---|
| Test Case ID | TC-INV-001 |
| Module | Inventory |
| Priority | P1 |
| Test Type | Functional |
| Preconditions | Stock receipt has been validated |
| Test Data | CMP001 — 100 Units received |

**Test Steps**

1. Open Inventory.
2. Navigate to the relevant product inventory report.
3. Search for CMP001.
4. Verify the on-hand quantity.
5. Compare the displayed quantity with the validated receipt and prior stock movements.

**Expected Results**

- The on-hand quantity reflects validated stock movements.
- No unexplained quantity discrepancy exists.
- The inventory movement history is available.

Actual Result: ____________________

Status: Not Executed

Evidence: ____________________

#### TC-INV-002 — Trigger Reordering Rule

| Attribute | Details |
|---|---|
| Test Case ID | TC-INV-002 |
| Module | Inventory / Purchase |
| Priority | P1 |
| Test Type | Functional |
| Preconditions | Reordering rule and vendor configuration are valid |
| Test Data | CMP001 minimum quantity 20 Units; maximum quantity 100 Units |

**Test Steps**

1. Configure a reordering rule for CMP001.
2. Verify its location, product, minimum, and maximum quantities.
3. Ensure the applicable replenishment route is configured.
4. Reduce forecasted stock below the configured minimum.
5. Execute the applicable replenishment scheduler or replenishment workflow.
6. Review the resulting replenishment proposal.

**Expected Results**

- The replenishment mechanism identifies the applicable shortage.
- A replenishment proposal or procurement document is generated according to the configured route.
- The replenishment quantity follows the configured rule and forecast calculations.
- No unexpected duplicate replenishment is created.

Actual Result: ____________________

Status: Not Executed

Evidence: ____________________

**Important test note:** Reordering rules may evaluate forecasted quantity rather than simply comparing on-hand quantity with the minimum. Incoming receipts, outgoing demand, reservations, locations, routes, and scheduler execution can affect the result. Test the actual forecast and configuration, not only the physical stock number.

#### TC-INV-003 — Prevent Negative Inventory Through Approved Controls

| Attribute | Details |
|---|---|
| Test Case ID | TC-INV-003 |
| Module | Inventory |
| Priority | P2 |
| Test Type | Negative |
| Preconditions | Stock-control policy is defined |
| Test Data | Attempt to process an outgoing quantity exceeding available stock |

**Test Steps**

1. Select a component with insufficient available quantity.
2. Create an outgoing stock operation.
3. Enter a quantity exceeding the available stock.
4. Attempt validation.

**Expected Results**

- The system behaves according to the approved inventory policy.
- If negative stock is prohibited, the operation is blocked or appropriately controlled.
- If negative stock is permitted by configuration, the exception is visible and documented.

Actual Result: ____________________

Status: Not Executed

Evidence: ____________________

---

### 7.4 Manufacturing Execution

#### TC-MFG-001 — Create Manufacturing Order

| Attribute | Details |
|---|---|
| Test Case ID | TC-MFG-001 |
| Module | Manufacturing |
| Priority | P1 |
| Test Type | Functional |
| Preconditions | WP100 BoM is valid |
| Test Data | WP100 — 10 Units |

**Test Steps**

1. Open Manufacturing.
2. Create a new Manufacturing Order.
3. Select WP100.
4. Enter production quantity of 10 Units.
5. Select the appropriate BoM.
6. Save the Manufacturing Order.

**Expected Results**

- Manufacturing Order is created.
- Product and quantity are correct.
- The correct BoM is selected.
- Required components are populated.
- The MO has a valid initial status.

Actual Result: ____________________

Status: Not Executed

Evidence: ____________________

#### TC-MFG-002 — Confirm Manufacturing Order

| Attribute | Details |
|---|---|
| Test Case ID | TC-MFG-002 |
| Module | Manufacturing |
| Priority | P1 |
| Test Type | Functional |
| Preconditions | Draft MO exists |
| Test Data | WP100 — 10 Units |

**Test Steps**

1. Open the draft MO.
2. Review product and component requirements.
3. Confirm the Manufacturing Order.
4. Review generated work orders, if applicable.
5. Review the component reservation state.

**Expected Results**

- Manufacturing Order is confirmed.
- Required production operations are generated when routing is configured.
- Component demand is calculated correctly.
- Reservation status reflects actual inventory availability.

Actual Result: ____________________

Status: Not Executed

Evidence: ____________________

#### TC-MFG-003 — Reserve Required Components

| Attribute | Details |
|---|---|
| Test Case ID | TC-MFG-003 |
| Module | Manufacturing / Inventory |
| Priority | P1 |
| Test Type | Integration |
| Preconditions | Confirmed MO and component stock exist |
| Test Data | WP100 — 10 Units |

**Test Steps**

1. Open the Manufacturing Order.
2. Review required component quantities.
3. Trigger or perform the configured reservation workflow.
4. Verify component availability.
5. Review reserved quantities.

**Expected Results**

- Required components are reserved according to stock availability and configuration.
- Reserved quantities are traceable.
- Insufficient stock is clearly identified.
- No unintended over-reservation occurs.

Actual Result: ____________________

Status: Not Executed

Evidence: ____________________

#### TC-MFG-004 — Handle Insufficient Components

| Attribute | Details |
|---|---|
| Test Case ID | TC-MFG-004 |
| Module | Manufacturing / Inventory |
| Priority | P1 |
| Test Type | Negative |
| Preconditions | Confirmed MO exists |
| Test Data | At least one component has insufficient available stock |

**Test Steps**

1. Create an MO requiring a component with insufficient stock.
2. Attempt component reservation.
3. Review the reservation status.
4. Review replenishment options.

**Expected Results**

- The system identifies the shortage.
- The user can identify the affected component and required quantity.
- The MO does not falsely indicate that all required materials are available.
- The shortage can be handled through the approved procurement or inventory process.

Actual Result: ____________________

Status: Not Executed

Evidence: ____________________

#### TC-MFG-005 — Execute Work Orders

| Attribute | Details |
|---|---|
| Test Case ID | TC-MFG-005 |
| Module | Manufacturing |
| Priority | P1 |
| Test Type | Functional |
| Preconditions | Confirmed MO with routing and work orders |
| Test Data | Machining → Fabrication → Assembly → Testing |

**Test Steps**

1. Open the Manufacturing Order.
2. Navigate to its work orders.
3. Start the first operation.
4. Record the operation execution.
5. Complete the operation.
6. Continue through the remaining operations.
7. Review work order statuses.

**Expected Results**

- Work orders are generated from the configured routing.
- Each operation is associated with the correct work center.
- Operations can be processed according to the configured sequence and dependencies.
- Work order statuses reflect actual execution.
- Operation records are linked to the correct MO.

Actual Result: ____________________

Status: Not Executed

Evidence: ____________________

#### TC-MFG-006 — Consume Components

| Attribute | Details |
|---|---|
| Test Case ID | TC-MFG-006 |
| Module | Manufacturing / Inventory |
| Priority | P1 |
| Test Type | Integration |
| Preconditions | MO is ready for production and components are available |
| Test Data | WP100 production order |

**Test Steps**

1. Open the Manufacturing Order.
2. Review component demand.
3. Process the configured component consumption workflow.
4. Record actual consumption where supported.
5. Complete the relevant production operations.
6. Review stock movements.

**Expected Results**

- Component consumption is recorded.
- Consumption quantities follow the approved BoM or permitted actual-consumption adjustments.
- Inventory balances are updated according to validated movements.
- Consumption is traceable to the Manufacturing Order.

Actual Result: ____________________

Status: Not Executed

Evidence: ____________________

#### TC-MFG-007 — Produce Finished Goods

| Attribute | Details |
|---|---|
| Test Case ID | TC-MFG-007 |
| Module | Manufacturing / Inventory |
| Priority | P1 |
| Test Type | Integration |
| Preconditions | Required production steps are completed |
| Test Data | WP100 — 10 Units |

**Test Steps**

1. Open the Manufacturing Order.
2. Verify work order completion.
3. Verify component consumption.
4. Record production quantity.
5. Complete the MO.
6. Open inventory.
7. Verify the finished goods quantity and movement history.

**Expected Results**

- The Manufacturing Order can be completed according to the configured workflow.
- Finished goods are recorded in the appropriate location.
- Produced quantity is accurate.
- Inventory movements are traceable to the MO.
- No duplicate finished goods receipt is created.

Actual Result: ____________________

Status: Not Executed

Evidence: ____________________

#### TC-MFG-008 — Handle Production Scrap

| Attribute | Details |
|---|---|
| Test Case ID | TC-MFG-008 |
| Module | Manufacturing / Inventory |
| Priority | P2 |
| Test Type | Functional |
| Preconditions | MO is in progress and scrap workflow is configured |
| Test Data | 1 Unit of illustrative component scrap |

**Test Steps**

1. Open an active MO.
2. Initiate the configured scrap process.
3. Select the affected component or product.
4. Enter the scrap quantity.
5. Confirm the transaction.
6. Review stock movement and production records.

**Expected Results**

- Scrap is recorded against the correct product and quantity.
- The appropriate inventory movement is generated.
- Scrap is traceable to the production transaction.
- Production reporting reflects the scrap where supported.

Actual Result: ____________________

Status: Not Executed

Evidence: ____________________

#### TC-MFG-009 — Handle Rework

| Attribute | Details |
|---|---|
| Test Case ID | TC-MFG-009 |
| Module | Manufacturing / Quality |
| Priority | P2 |
| Test Type | Integration |
| Preconditions | Rework procedure has been defined and configured |
| Test Data | One WP100 unit requires rework |

**Test Steps**

1. Identify a failed or nonconforming product.
2. Create the applicable quality alert or nonconformance record.
3. Initiate the approved rework procedure.
4. Perform the required rework operations.
5. Record the inspection result.
6. Review the final product disposition.

**Expected Results**

- Rework is documented.
- The affected product is traceable.
- Rework activities follow the approved procedure.
- The product cannot be treated as accepted until the required inspection is completed.

Actual Result: ____________________

Status: Not Executed

Evidence: ____________________

---

### 7.5 Quality Management

#### TC-QA-001 — Create Quality Control Point

| Attribute | Details |
|---|---|
| Test Case ID | TC-QA-001 |
| Module | Quality |
| Priority | P1 |
| Test Type | Functional |
| Preconditions | Quality application is installed |
| Test Data | WP100 final inspection |

**Test Steps**

1. Open Quality.
2. Create a quality control point.
3. Select the applicable product or operation.
4. Configure the inspection frequency and control type.
5. Save the configuration.
6. Verify the resulting quality check behavior.

**Expected Results**

- Quality control point is saved successfully.
- The configured product or operation is correct.
- The control point triggers checks according to its configuration.

Actual Result: ____________________

Status: Not Executed

Evidence: ____________________

#### TC-QA-002 — Pass Quality Inspection

| Attribute | Details |
|---|---|
| Test Case ID | TC-QA-002 |
| Module | Quality |
| Priority | P1 |
| Test Type | Functional |
| Preconditions | Quality check exists |
| Test Data | WP100 — inspection result Pass |

**Test Steps**

1. Open the generated quality check.
2. Inspect the relevant product.
3. Enter the required measurement or result.
4. Mark the inspection as passed.
5. Review the quality record.

**Expected Results**

- Inspection result is recorded successfully.
- Result is linked to the appropriate product or operation.
- The inspection is traceable.
- The configured workflow proceeds according to the passing result.

Actual Result: ____________________

Status: Not Executed

Evidence: ____________________

#### TC-QA-003 — Fail Quality Inspection

| Attribute | Details |
|---|---|
| Test Case ID | TC-QA-003 |
| Module | Quality |
| Priority | P1 |
| Test Type | Negative |
| Preconditions | Quality check exists |
| Test Data | WP100 — inspection result Fail |

**Test Steps**

1. Open a quality check.
2. Enter an out-of-specification result.
3. Mark the inspection as failed.
4. Review the resulting quality alert or exception workflow.
5. Verify the product disposition.

**Expected Results**

- Failed inspection is recorded.
- The failure is traceable.
- The configured exception process is initiated.
- The product is handled according to the approved quality disposition policy.

Actual Result: ____________________

Status: Not Executed

Evidence: ____________________

#### TC-QA-004 — Record Nonconformance

| Attribute | Details |
|---|---|
| Test Case ID | TC-QA-004 |
| Module | Quality |
| Priority | P2 |
| Test Type | Functional |
| Preconditions | Quality alert workflow is available |
| Test Data | Illustrative defective WP100 unit |

**Test Steps**

1. Create a quality alert.
2. Select the affected product.
3. Enter the defect description.
4. Record the responsible process or work center.
5. Assign the responsible user.
6. Save the record.
7. Review its status and traceability.

**Expected Results**

- Quality alert is created successfully.
- Defect details are recorded.
- The responsible process or work center is identifiable.
- The record can be tracked through its configured resolution workflow.

Actual Result: ____________________

Status: Not Executed

Evidence: ____________________

---

### 7.6 Manufacturing Costing and Accounting

#### TC-CST-001 — Validate Manufacturing Cost Inputs

| Attribute | Details |
|---|---|
| Test Case ID | TC-CST-001 |
| Module | Manufacturing |
| Priority | P1 |
| Test Type | Functional |
| Preconditions | BoM and costing-related configuration exist |
| Test Data | WP100 BoM and illustrative component costs |

**Test Steps**

1. Open the WP100 BoM.
2. Review component quantities.
3. Review the configured component cost data.
4. Review applicable operation or work center cost settings.
5. Compare the expected cost inputs with the approved illustrative cost model.

**Expected Results**

- Cost inputs are available as configured.
- Component quantities and cost assumptions are consistent.
- Applicable work center costs are configured where required.
- The costing method is documented.

Actual Result: ____________________

Status: Not Executed

Evidence: ____________________

#### TC-CST-002 — Validate Manufacturing Cost Calculation

| Attribute | Details |
|---|---|
| Test Case ID | TC-CST-002 |
| Module | Manufacturing / Accounting |
| Priority | P1 |
| Test Type | Integration |
| Preconditions | Costing configuration is defined |
| Test Data | Completed WP100 MO |

**Test Steps**

1. Complete a test Manufacturing Order.
2. Review its cost analysis or related valuation records.
3. Compare the resulting cost with the expected calculation.
4. Verify the applicable cost components.
5. Review accounting impact if automated valuation is configured.

**Expected Results**

- Cost information is calculated according to the configured costing methodology.
- Cost components can be reconciled with the applicable inputs.
- Accounting entries, if applicable, are consistent with the configured valuation method.
- Differences are explainable and documented.

Actual Result: ____________________

Status: Not Executed

Evidence: ____________________

**Important:** Do not assume that every Odoo costing configuration produces the same accounting entries. Product costing method, inventory valuation, work center configuration, and installed applications affect the expected result. Define the expected accounting outcome only after the actual configuration is confirmed.

---

## 8. Integration and End-to-End Test Scenarios

### 8.1 E2E-001 — Procurement to Component Inventory

**Objective:** Verify that purchased components can be received and made available for manufacturing.

**Preconditions:**

- Vendor exists.
- Component product exists.
- Purchase application is installed.
- Inventory routes and locations are configured.

**Scenario:**

1. Create an RFQ.
2. Add CMP001.
3. Confirm the Purchase Order.
4. Open the associated receipt.
5. Validate the receipt.
6. Verify inventory on-hand quantity.
7. Verify the stock movement history.

**Expected Results:**

- Purchase Order is confirmed.
- Receipt is generated and validated.
- Stock quantity is updated correctly.
- Receipt is traceable to the Purchase Order.

**Related Test Cases:** TC-PUR-001, TC-PUR-002, TC-INV-001.

Status: Not Executed

Evidence: ____________________

### 8.2 E2E-002 — Manufacturing Order to Finished Goods

**Objective:** Verify the complete manufacturing process.

**Preconditions:**

- WP100 product exists.
- WP100 BoM is valid.
- Routing is configured.
- Work centers are available.
- Required component stock is available.

**Scenario:**

1. Create an MO for 10 WP100 units.
2. Confirm the MO.
3. Verify component demand.
4. Reserve components.
5. Execute Machining.
6. Execute Fabrication.
7. Execute Assembly.
8. Execute Testing.
9. Record required component consumption.
10. Complete the MO.
11. Verify finished goods inventory.

**Expected Results:**

- MO is confirmed successfully.
- Required work orders are generated.
- Work center assignments are correct.
- Component consumption is recorded.
- Finished goods are received into the configured stock location.
- All related transactions are traceable.

**Related Test Cases:** TC-MFG-001 through TC-MFG-007.

Status: Not Executed

Evidence: ____________________

### 8.3 E2E-003 — Material Shortage and Replenishment

**Objective:** Verify how the ERP handles insufficient component inventory.

**Preconditions:**

- Reordering rules are configured.
- Procurement routes are valid.
- Test component stock can be controlled.

**Scenario:**

1. Reduce CMP001 stock below the applicable replenishment threshold.
2. Create or review manufacturing demand.
3. Verify forecasted stock.
4. Execute the applicable replenishment workflow.
5. Review the replenishment proposal.
6. Confirm the generated procurement document if applicable.
7. Receive the component.
8. Verify stock availability.
9. Retry the manufacturing reservation.

**Expected Results:**

- Shortage is identified.
- Replenishment is generated according to the configured route.
- Procurement and receipt are traceable.
- Components become available for the manufacturing workflow.

**Related Test Cases:** TC-INV-002, TC-MFG-003, TC-MFG-004, TC-PUR-002.

Status: Not Executed

Evidence: ____________________

### 8.4 E2E-004 — Quality Failure and Rework

**Objective:** Verify nonconformance handling and product disposition.

**Preconditions:**

- Quality checks are configured.
- Rework process is documented.
- Relevant users have permissions.

**Scenario:**

1. Create or execute a WP100 quality check.
2. Record an inspection failure.
3. Create or review the associated quality alert.
4. Identify the affected product.
5. Initiate the approved rework workflow.
6. Complete rework.
7. Perform a follow-up inspection.
8. Record the final disposition.

**Expected Results:**

- Failed inspection is documented.
- Quality alert is traceable.
- Rework is controlled.
- Product disposition is documented.
- The final quality result is available.

**Related Test Cases:** TC-QA-003, TC-QA-004, TC-MFG-009.

Status: Not Executed

Evidence: ____________________

### 8.5 E2E-005 — Production Cost Review

**Objective:** Verify manufacturing cost visibility.

**Preconditions:**

- Costing configuration is finalized.
- Component costs are available.
- Work center costs are configured where required.

**Scenario:**

1. Create and complete a test MO.
2. Review component consumption.
3. Review production operation information.
4. Review cost analysis.
5. Compare the result with the illustrative cost calculation.
6. Verify accounting impact if configured.

**Expected Results:**

- Relevant cost inputs are traceable.
- Cost analysis is consistent with the configured method.
- Variances are documented.
- Accounting impact is explainable.

**Related Test Cases:** TC-CST-001, TC-CST-002.

Status: Not Executed

Evidence: ____________________

---

## 9. Security and Access Control Testing

### 9.1 Security Test Cases

#### TC-SEC-001 — Manufacturing User Access

| Attribute | Details |
|---|---|
| Test Case ID | TC-SEC-001 |
| Priority | P1 |
| Test Type | Security |
| Preconditions | TEST-MFG-USER exists |

**Test Steps**

1. Log in as TEST-MFG-USER.
2. Open Manufacturing.
3. Attempt to access permitted manufacturing operations.
4. Attempt to access restricted system configuration.
5. Verify visible menus and available actions.

**Expected Results**

- User can access authorized manufacturing functions.
- User cannot access restricted configuration without permission.
- Access restrictions behave according to the approved role matrix.

Status: Not Executed

Evidence: ____________________

#### TC-SEC-002 — Warehouse User Access

| Attribute | Details |
|---|---|
| Test Case ID | TC-SEC-002 |
| Priority | P1 |
| Test Type | Security |
| Preconditions | TEST-WH-MGR exists |

**Test Steps**

1. Log in as TEST-WH-MGR.
2. Open Inventory.
3. Perform permitted stock operations.
4. Attempt to access restricted manufacturing or accounting functions.
5. Verify access behavior.

**Expected Results**

- Authorized inventory operations are available.
- Restricted functions remain inaccessible unless explicitly granted.
- No unauthorized data modification is possible.

Status: Not Executed

Evidence: ____________________

#### TC-SEC-003 — Unauthorized Configuration Changes

| Attribute | Details |
|---|---|
| Test Case ID | TC-SEC-003 |
| Priority | P1 |
| Test Type | Negative Security |
| Preconditions | A non-administrator test user exists |

**Test Steps**

1. Log in as a non-administrator user.
2. Attempt to modify restricted system configuration.
3. Attempt direct access to restricted menus or records.
4. Verify the system response.

**Expected Results**

- Unauthorized changes are blocked.
- Restricted records cannot be modified through alternative navigation paths.
- Access-denied behavior is recorded.

Status: Not Executed

Evidence: ____________________

#### TC-SEC-004 — Multi-Company Data Isolation

| Attribute | Details |
|---|---|
| Test Case ID | TC-SEC-004 |
| Priority | P2 |
| Test Type | Security |
| Preconditions | Multi-company configuration is enabled |

**Test Steps**

1. Create two test companies.
2. Create test records assigned to each company.
3. Log in as a user restricted to one company.
4. Attempt to view records belonging to the other company.
5. Verify access restrictions.

**Expected Results**

- Users can access only authorized company records.
- Cross-company visibility follows the approved access policy.
- No unintended data leakage occurs.

Status: Not Executed

Evidence: ____________________

**Applicability:** Execute this test only if multi-company operation is included in the actual project scope.

---

## 10. Non-Functional Testing

### 10.1 Performance Testing

Performance testing should measure actual behavior under a representative workload.

Proposed illustrative test profile:

| Parameter | Proposed Value |
|---|---:|
| Concurrent Users | 30 |
| Test Duration | 15 minutes |
| Test Environment | Staging |
| Primary Operations | Login, search, MO creation, inventory lookup |
| Availability Target | 99.5% monthly, subject to validation |

The workload and thresholds must be reviewed against the final infrastructure sizing and business requirements.

#### TC-NFR-001 — Concurrent User Performance

**Test Steps**

1. Prepare a staging environment.
2. Create representative user accounts.
3. Execute concurrent login and navigation requests.
4. Simulate representative manufacturing and inventory operations.
5. Collect response-time and error-rate metrics.
6. Review application and database resource utilization.

**Expected Results**

- No critical application errors occur.
- The system remains usable under the agreed workload.
- Response times meet the approved performance targets.
- Database and application resource utilization remain within agreed limits.

Status: Not Executed

Evidence: ____________________

#### TC-NFR-002 — Manufacturing Order Processing Performance

**Test Steps**

1. Prepare representative BoMs.
2. Generate multiple test Manufacturing Orders.
3. Execute the approved MO creation and confirmation workload.
4. Measure response times.
5. Review application and database logs.

**Expected Results**

- MO processing completes successfully.
- No data corruption or duplicate transactions occur.
- Performance meets the approved target.

Status: Not Executed

Evidence: ____________________

### 10.2 Reliability Testing

#### TC-NFR-003 — Application Restart Recovery

**Test Steps**

1. Confirm a clean application state.
2. Stop the Odoo systemd service using the approved procedure.
3. Restart the service.
4. Verify application availability.
5. Review logs for startup errors.
6. Verify database connectivity.

**Expected Results**

- Odoo restarts successfully.
- Existing database records remain intact.
- The service becomes available.
- No unexpected migration or data loss occurs.

Status: Not Executed

Evidence: ____________________

### 10.3 Backup and Recovery Testing

#### TC-DR-001 — Database and Filestore Backup

**Test Steps**

1. Confirm the backup schedule and retention policy.
2. Generate a database backup.
3. Generate the corresponding filestore backup.
4. Verify backup file integrity.
5. Record backup timestamps.
6. Verify both backups represent a consistent recovery point.

**Expected Results**

- Database backup is generated successfully.
- Filestore backup is generated successfully.
- Backup files are stored in the approved location.
- Backup completion is logged.
- Recovery point consistency is documented.

Status: Not Executed

Evidence: ____________________

#### TC-DR-002 — Restore Test Environment

**Test Steps**

1. Select a verified backup.
2. Prepare an isolated restoration environment.
3. Restore the PostgreSQL database.
4. Restore the corresponding filestore.
5. Configure the restored Odoo environment.
6. Start Odoo.
7. Verify key business records.
8. Verify product attachments and related files.
9. Record restoration duration.

**Expected Results**

- Database restoration completes successfully.
- Filestore files are accessible.
- Odoo starts without critical errors.
- Key manufacturing, inventory, and procurement records are available.
- Actual recovery time and recovery point are recorded.

Status: Not Executed

Evidence: ____________________

**Important:** A successful backup job is not proof of recoverability. A restoration test is required.

---

## 11. Regression Testing

### 11.1 Purpose

Regression testing ensures that new changes do not break previously validated functionality.

Regression testing must be performed after:

- Custom module changes.
- Odoo configuration changes affecting business workflows.
- Application upgrades.
- Python dependency changes.
- Database migrations.
- Security rule changes.
- Deployment of bug fixes.

### 11.2 Regression Test Suite

| Test ID | Scenario | Priority |
|---|---|---|
| REG-001 | Product creation and editing | P2 |
| REG-002 | BoM creation and validation | P1 |
| REG-003 | Routing and work center assignment | P1 |
| REG-004 | Purchase Order confirmation | P1 |
| REG-005 | Component receipt and stock update | P1 |
| REG-006 | Reordering rule execution | P1 |
| REG-007 | Manufacturing Order confirmation | P1 |
| REG-008 | Work order execution | P1 |
| REG-009 | Component consumption | P1 |
| REG-010 | Finished goods production | P1 |
| REG-011 | Quality inspection | P1 |
| REG-012 | User access permissions | P1 |
| REG-013 | Manufacturing cost review | P2 |
| REG-014 | Backup and restoration | P1 |

### 11.3 Regression Exit Criteria

Regression testing can be considered complete when:

- All critical regression cases have been executed.
- No unresolved critical defects remain.
- High-priority defects are resolved or formally accepted.
- Failed test cases have been investigated.
- Results and evidence are recorded.

---

## 12. User Acceptance Testing

### 12.1 UAT Objectives

UAT validates whether the system supports the expected business workflows from the perspective of the intended users.

UAT is not a substitute for technical testing. It should be conducted after critical functional and integration defects have been resolved.

### 12.2 UAT Scenarios

| UAT ID | Business Role | Scenario |
|---|---|---|
| UAT-001 | Production Manager | Create and monitor Manufacturing Orders |
| UAT-002 | Production Supervisor | Execute work orders |
| UAT-003 | Warehouse Manager | Receive and issue components |
| UAT-004 | Procurement Manager | Create and manage Purchase Orders |
| UAT-005 | Quality Manager | Record inspection results |
| UAT-006 | Finance Manager | Review manufacturing cost information |
| UAT-007 | IT Administrator | Validate user access and system availability |

### 12.3 UAT Execution Template

For each UAT scenario:

1. Assign the responsible business role.
2. Explain the business scenario.
3. Provide controlled test data.
4. Ask the participant to execute the workflow.
5. Record observations.
6. Capture any defects.
7. Obtain the participant's actual acceptance decision.

### 12.4 UAT Sign-Off Template

| Field | Value |
|---|---|
| UAT Scenario ID | |
| Business Role | |
| Participant | |
| Execution Date | |
| Result | Pass / Fail / Blocked |
| Business Comments | |
| Outstanding Issues | |
| Acceptance Decision | Accepted / Rejected / Conditional |
| Approval Reference | |

**Portfolio note:** Leave participant names, actual execution dates, and approvals blank unless genuine UAT activities have taken place. A simulated UAT result must be clearly labeled as simulated.

---

## 13. Defect Management

### 13.1 Defect Lifecycle

The proposed defect lifecycle is:

1. New
2. Assigned
3. In Progress
4. Fixed
5. Ready for Retest
6. Retest Passed
7. Closed

Additional states:

- Reopened
- Rejected
- Deferred
- Duplicate

### 13.2 Defect Severity

| Severity | Definition | Example |
|---|---|---|
| Critical | System unusable or severe data integrity issue | Production transactions corrupt inventory |
| High | Major business workflow blocked | Manufacturing Order cannot be completed |
| Medium | Partial functionality affected | Incorrect report calculation |
| Low | Minor issue | UI label or alignment problem |

### 13.3 Defect Priority

| Priority | Definition |
|---|---|
| P1 | Must be resolved before release |
| P2 | Should be resolved before release |
| P3 | Can be scheduled for a later release |
| P4 | Cosmetic or low-impact enhancement |

Severity measures the impact of the defect. Priority determines how urgently it must be resolved. They should not be treated as interchangeable.

### 13.4 Defect Report Template

| Field | Description |
|---|---|
| Defect ID | Unique defect reference |
| Title | Short issue description |
| Related Test Case | Test case ID |
| Module | Affected Odoo module |
| Environment | Dev / QA / Staging |
| Severity | Critical / High / Medium / Low |
| Priority | P1 / P2 / P3 / P4 |
| Preconditions | Required conditions |
| Steps to Reproduce | Reproducible procedure |
| Expected Result | Correct system behavior |
| Actual Result | Observed behavior |
| Evidence | Screenshot, log, or record reference |
| Assigned To | Responsible developer |
| Status | Current defect state |
| Resolution | Fix description |
| Retest Result | Pass / Fail |

### 13.5 Defect Handling Rules

- Every defect must have a unique ID.
- Every defect must reference a test case or requirement where applicable.
- Critical and high-severity defects must be reviewed before release.
- Fixed defects must be retested.
- Reopened defects must retain their original reference.
- Deferred defects must have a documented rationale and approval.
- Defect closure must be supported by evidence.

---

## 14. Test Execution and Reporting

### 14.1 Test Case Execution Status

Each test case must use one of the following statuses:

| Status | Meaning |
|---|---|
| Not Executed | Test has not started |
| In Progress | Test is being executed |
| Passed | Expected result achieved |
| Failed | Expected result not achieved |
| Blocked | Test cannot proceed |
| Not Applicable | Test is outside the applicable scope |

### 14.2 Test Execution Record

| Field | Value |
|---|---|
| Test Case ID | |
| Tester | |
| Environment | |
| Execution Date | |
| Build / Commit Reference | |
| Test Data Reference | |
| Actual Result | |
| Status | |
| Defect ID | |
| Evidence Reference | |
| Comments | |

### 14.3 Test Summary Metrics

The following metrics should be reported:

**Total Test Cases**

\[
N_{total} = N_{passed}+N_{failed}+N_{blocked}+N_{not\ executed}
\]

**Pass Rate**

\[
Pass\ Rate =
\frac{N_{passed}}{N_{executed}}\times100\%
\]

Where:

\[
N_{executed}=N_{passed}+N_{failed}
\]

**Defect Density**

\[
Defect\ Density =
\frac{N_{valid\ defects}}{N_{tested\ functional\ areas}}
\]

**Test Coverage**

\[
Test\ Coverage =
\frac{N_{requirements\ with\ test\ coverage}}
{N_{in\ scope\ requirements}}\times100\%
\]

Metrics must be calculated from actual execution records. Do not report hypothetical pass rates as achieved project results.

### 14.4 Test Summary Report Template

| Metric | Result |
|---|---:|
| Total Test Cases | |
| Passed | |
| Failed | |
| Blocked | |
| Not Executed | |
| Pass Rate | |
| Requirements Covered | |
| Requirement Coverage | |
| Critical Defects Open | |
| High Defects Open | |
| Medium Defects Open | |
| Low Defects Open | |

### 14.5 Test Execution Evidence

Recommended evidence:

- Screenshots of completed transactions.
- Manufacturing Order references.
- Work Order references.
- Inventory movement records.
- Purchase Order and receipt references.
- Quality check and alert references.
- Cost analysis reports.
- Application logs.
- PostgreSQL backup and restoration records.
- Automated test output.
- Performance test reports.
- Defect records.

Evidence should be stored in a controlled project directory, for example:

```text
documentations/
└── test-evidence/
    ├── 01_master_data/
    ├── 02_bom_routing/
    ├── 03_procurement/
    ├── 04_inventory/
    ├── 05_manufacturing/
    ├── 06_quality/
    ├── 07_costing/
    ├── 08_security/
    ├── 09_performance/
    ├── 10_backup_recovery/
    └── 11_uat/
```

---

## 15. Entry and Exit Criteria

### 15.1 Test Entry Criteria

Testing may begin when:

- Odoo 19 is installed and accessible.
- PostgreSQL is operational.
- Required applications are installed.
- Relevant configurations are complete.
- Required master data is available.
- Test users and access rights are configured.
- Test database is isolated.
- Test cases are reviewed.
- Test environment readiness checks pass.

### 15.2 Functional Testing Exit Criteria

Functional testing may be considered complete when:

- All planned critical test cases have been executed.
- All critical test cases pass.
- High-priority failures are resolved or formally accepted.
- Remaining defects are documented.
- Test evidence is available.
- Requirement traceability is reviewed.

### 15.3 UAT Exit Criteria

UAT may be considered complete when:

- All in-scope UAT scenarios have been executed.
- Business users have reviewed the results.
- Critical business issues are resolved.
- Outstanding issues are documented.
- Actual acceptance decisions are recorded.
- The authorized approver provides sign-off.

### 15.4 Production Release Gate

Production deployment must not proceed solely because the test suite has a high pass rate.

The release decision must also consider:

- Critical defect status.
- High-risk business process coverage.
- Data migration readiness, if applicable.
- Backup and recovery verification.
- Security configuration.
- User training readiness.
- Operational support readiness.
- Actual UAT acceptance.
- Deployment and rollback readiness.

---

## 16. Risk Assessment

| Risk ID | Risk Description | Impact | Mitigation |
|---|---|---|---|
| RISK-001 | Incorrect BoM configuration | Incorrect component demand | Validate BoM against engineering specification |
| RISK-002 | Incorrect work center assignment | Work orders routed incorrectly | Validate routing configuration |
| RISK-003 | Inventory discrepancy | Production interruption | Reconcile stock movements |
| RISK-004 | Incorrect replenishment configuration | Excess or insufficient stock | Test forecast and replenishment routes |
| RISK-005 | Incorrect component consumption | Incorrect inventory and cost | Validate consumption records |
| RISK-006 | Quality failure not controlled | Nonconforming goods released | Validate quality exception workflow |
| RISK-007 | Incorrect costing configuration | Misleading manufacturing cost | Validate costing methodology |
| RISK-008 | Excessive user permissions | Unauthorized data access | Test role-based access |
| RISK-009 | Failed backup restoration | Business data unavailable | Perform restoration tests |
| RISK-010 | Configuration changes introduce regression | Existing functions break | Execute regression test suite |

---

## 17. Test Deliverables

The testing phase should produce the following deliverables:

| Deliverable | Description |
|---|---|
| Test Strategy | Overall testing approach |
| Test Case Specification | Detailed test procedures |
| Requirement Traceability Matrix | Mapping between requirements and tests |
| Test Data Specification | Controlled test data |
| Test Execution Records | Actual test results |
| Defect Register | Identified issues |
| Regression Test Report | Regression execution results |
| UAT Report | Business acceptance results |
| Performance Test Report | Performance observations |
| Backup & Recovery Report | Restoration evidence |
| Test Summary Report | Overall testing outcome |
| Release Recommendation | Go / No-Go recommendation |

---

## 18. Final Acceptance Criteria

The proposed system is considered ready for release only when all applicable acceptance criteria are satisfied.

| ID | Acceptance Criteria | Verification |
|---|---|---|
| TEST-AC-001 | Required master data can be created and maintained | Functional tests |
| TEST-AC-002 | BoMs are correctly configured | BoM validation |
| TEST-AC-003 | Routing operations use valid work centers | Routing tests |
| TEST-AC-004 | Procurement transactions work correctly | Procurement tests |
| TEST-AC-005 | Inventory movements are accurate | Inventory tests |
| TEST-AC-006 | Reordering rules work as configured | Replenishment tests |
| TEST-AC-007 | Manufacturing Orders can be created and processed | Manufacturing tests |
| TEST-AC-008 | Work orders follow the configured routing | Work order tests |
| TEST-AC-009 | Component consumption is recorded accurately | Inventory integration tests |
| TEST-AC-010 | Finished goods are recorded correctly | Production completion tests |
| TEST-AC-011 | Quality inspections are recorded correctly | Quality tests |
| TEST-AC-012 | Nonconformance handling is traceable | Quality exception tests |
| TEST-AC-013 | Cost information follows the configured methodology | Costing tests |
| TEST-AC-014 | User access follows the approved role matrix | Security tests |
| TEST-AC-015 | Backup and restoration are verified | Disaster recovery tests |
| TEST-AC-016 | Critical regression tests pass | Regression report |
| TEST-AC-017 | Required UAT scenarios are accepted | UAT report |
| TEST-AC-018 | No unresolved release-blocking defects remain | Defect register |

These are project-level proposed test acceptance criteria. They must be reconciled with the original business acceptance criteria AC-001 through AC-048 before final approval.

---

## 19. Approval and Sign-Off

The following approval table is a template only.

| Role | Name | Decision | Date | Signature / Reference |
|---|---|---|---|---|
| Project Sponsor | | Pending | | |
| Manufacturing Manager | | Pending | | |
| Warehouse Manager | | Pending | | |
| Quality Manager | | Pending | | |
| Finance Manager | | Pending | | |
| IT Administrator | | Pending | | |
| QA Lead | | Pending | | |

No approval should be represented as completed until the responsible person has actually reviewed and approved the deliverable.

---

## 20. Assumptions and Constraints

### 20.1 Assumptions

- The target ERP is Odoo 19.
- PostgreSQL is used as the database.
- Installation and deployment do not use Docker.
- Required Odoo applications are available and installed.
- The manufacturing environment is represented by one hypothetical facility.
- WP100 and EM200 are illustrative manufactured products.
- Machining, Fabrication, Assembly, and Testing are illustrative work centers.
- All test data is synthetic.
- The final test configuration will be aligned with the approved Functional Specification.

### 20.2 Constraints

- Odoo features depend on the installed edition and applications.
- Custom modules require additional unit and integration testing.
- Actual business acceptance requires real authorized participants.
- Performance results depend on the final infrastructure.
- Accounting outcomes depend on the configured costing and valuation methodology.
- Test results cannot be claimed until test execution has occurred.

---

## 21. Final Notes

This document establishes the testing foundation for the Astra Manufacturing ERP implementation.

The testing approach prioritizes the integrity of manufacturing and inventory transactions, accurate production execution, controlled quality processes, and reliable business data.

Before the test phase is formally approved:

1. Reconcile all test cases with the final Business Requirements Document.
2. Complete the Requirement Traceability Matrix.
3. Verify the actual Odoo 19 application and edition configuration.
4. Confirm the BoM, routing, and inventory test fixtures.
5. Prepare isolated test and UAT environments.
6. Execute the test cases and record genuine results.
7. Resolve release-blocking defects.
8. Obtain actual UAT acceptance.

The project must distinguish between documented test procedures, simulated examples, executed tests, and formally accepted results.

A well-defined test strategy does not prove that an ERP implementation works. Only reproducible execution, supporting evidence, and authorized acceptance can establish that conclusion.

---

**End of Document**

**Document:** `05_test_strategy_and_test_cases.md`  
**Project:** Astra Manufacturing — Manufacturing & Production Management ERP  
**Version:** 1.0  
**Status:** Draft — Portfolio Simulation