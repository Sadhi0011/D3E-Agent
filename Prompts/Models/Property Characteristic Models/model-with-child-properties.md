# Model with Child Properties

## Context

A child property is a property that is conceptually a part of another entity, often referred to as the parent entity. Child properties are dependent on the existence of the parent entity and do not exist independently. They are typically saved or deleted along with the parent. Child properties are useful when you have a hierarchical or composition relationship, and the child properties are closely tied to the existence of the parent entity.

- **Independence:** Child properties do not exist independently. They are part of the parent entity and are managed together.

## Prompt for Creating

"Create a [ModelName] model with child property [propertyName] of type [ChildModelName]"

**Example Prompts:**

- "Create a Customer model with name, email, phone number, and a collection of addresses as child properties where each address contains street, city, state, and zip code"
- "Create a Lead model with a child property Education History of type Education (collection)"
- "Create an Order model with order number, customer email, order date, total amount, and a collection of order items as child properties where each item has product name, quantity, and price"
-

## D3E Examples

### Example 1: Lead with Education History (Child Collection)

```d3e
Model {
    name 'Lead'
    properties [
        {
            name 'Name'
            type String
            required true
        }
        {
            name 'Email'
            type String
            required true
        }
        {
            name 'Phone Number'
            type String
        }
        {
            name 'Education History'
            collection true
            type Education
            child true
        }
        {
            name 'Created By'
            type User
        }
    ]
}

Model {
    name 'Education'
    creatable false
    properties [
        {
            name 'Institution'
            type String
            required true
        }
        {
            name 'Degree'
            type String
            required true
        }
        {
            name 'Field of Study'
            type String
        }
        {
            name 'Start Date'
            type Date
            required true
        }
        {
            name 'End Date'
            type Date
        }
    ]
}
```

### Example 2: FamilyInfo with Children (Child Collection)

```d3e
Model {
    name 'Family Info'
    properties [
        {
            name 'Spouse Name'
            type String
        }
        {
            name 'Marrital Status'
            type MaritalStatus
        }
        {
            name 'Family Income'
            type Double
        }
        {
            name 'Family Members'
            type Integer
        }
        {
            name 'Children'
            type Child
            collection true
            child true
        }
        {
            name 'has Elderly Care Responsibility'
            type Boolean
        }
        {
            name 'annisversary Date'
            type Date
        }
    ]
}

Model {
    name 'Child'
    creatable false
    properties [
        {
            name 'age Group'
            type String
        }
        {
            name 'Name'
            type String
        }
    ]
}
```

**Note:**

- The `child true` attribute marks the property as a child property.
- Child models (like `Education` or `Child`) are often marked as `creatable false` to prevent them from being created independently of their parent.
- Collections of child properties are supported (e.g., a Lead can have multiple Education records).
