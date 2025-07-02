# D3E Models Guide

## Introduction

In D3E Studio, **models** are fundamental building blocks that define the structure and characteristics of data within your application. Models act as blueprints for creating, storing, and interacting with information, and are central to both backend and frontend development in D3E.

---

## Types of Models in D3E

D3E supports several types of models, each serving a specific purpose:

| Model Type   | Description |
|--------------|-------------|
| **Standard Model** | Represents persistent data stored in the database (e.g., User, Contact, Invoice). Used for CRUD operations and API generation. |
| **Embedded Model** | Used as a nested, always-present part of another model. Not stored independently; always exists as part of its parent. |
| **Non-Creatable Model** | Used internally as part of other models, but cannot be created or managed directly via API. |
| **Struct** | Similar to models, but not stored in the database. Used for temporary data transfer (e.g., between server and client, or between components). |

---

## Model Properties

Each model consists of **properties** that define the fields and data types for the model. Properties can have various attributes that control their behavior and usage.

### Common Property Attributes

| Attribute         | Description |
|-------------------|-------------|
| **Name**          | The unique identifier for the property within the model. |
| **Type**          | The data type of the property (e.g., String, Integer, Boolean, another Model, OptionSet). |
| **Required**      | If true, the property must have a value when creating or updating the model. |
| **Collection**    | If true, the property holds a list of values instead of a single value. |
| **Default Value** | The value assigned if none is provided during creation. |
| **Reference From**| Indicates a reference to another property or model, establishing relationships. |
| **Exists If**     | Conditional logic to determine if the property should exist based on other values. |
| **Description**   | Human-readable explanation of the property's purpose. |
| **Read Type**     | Controls access: Read/Write, Write Once, Read Only, Local. |
| **Computed**      | The property's value is calculated dynamically from other properties. |
| **Transient**     | Not stored in the database; used for temporary or calculated values. |
| **Unique**        | Ensures the property value is unique across all records. |

---

## Example: Model Definition

```yaml
Model: User
  properties:
    - name: "email"
      type: "String"
      required: true
      unique: true
      description: "User's email address. Must be unique."
    - name: "password"
      type: "String"
      required: true
      description: "Hashed password for authentication."
    - name: "roles"
      type: "String"
      collection: true
      default: []
      description: "List of roles assigned to the user."
    - name: "profile"
      type: "Profile"
      embedded: true
      description: "Embedded profile information."
    - name: "createdAt"
      type: "DateTime"
      default: "now()"
      readType: "Read Only"
      description: "Timestamp when the user was created."
```

---

## Brief Explanation of Key Property Types

| Property Type | Description |
|---------------|-------------|
| **Primitive** | Basic types: String, Integer, Double, Boolean, Date, Time, DateTime, File, Duration. |
| **Model Reference** | Points to another model, establishing relationships (e.g., User has a reference to Company). |
| **OptionSet** | Restricts the value to a predefined set of options (like enums). |
| **Collection** | Indicates the property is a list/array of the specified type. |
| **Embedded** | The property is always present as part of the parent model and cannot be null. |
| **Computed** | Value is calculated from other properties using an expression. |
| **Transient** | Used for temporary/calculated data, not persisted in the database. |

---

## Special Model Features

- **Validations**: Rules to ensure data integrity (e.g., email format, value ranges).
- **Actions**: Custom logic or methods attached to models (e.g., createUser, resetPassword).
- **Access Controls**: Define who can read/write/update/delete model records.
- **Inheritance**: Models can extend other models, inheriting their properties and behaviors.

---

## Summary Table: Model Property Attributes

| Attribute      | Example Value | Purpose |
|----------------|--------------|---------|
| Name           | "email"      | Field identifier |
| Type           | "String"     | Data type |
| Required       | true          | Must be provided |
| Collection     | false         | Single value |
| Default Value  | ""           | Initial value |
| Unique         | true          | No duplicates |
| Computed       | "quantity * price" | Calculated value |
| Transient      | true          | Not stored in DB |
| Description    | "User's email address" | Field purpose |

---

## Conclusion

Models are the backbone of D3E applications, defining the structure, relationships, and rules for your data. Understanding model types and property attributes is essential for effective D3E development.

For more details, refer to the `/d3e/models.md` and `/d3e/development/model.md` files in your project. 