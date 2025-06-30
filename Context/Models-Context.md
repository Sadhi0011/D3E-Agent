# D3E Studio Model Generation Context

## Overview
D3E Studio is a low-code platform that generates 90% of backend applications from model definitions. Models represent data objects and their relationships, forming the foundation of your application.

## D3E Model Syntax Structure

### Basic Model Declaration
```
Model {
    name '[ModelName]'
    [optional: package '[package.name]']
    [optional: parent [ParentModel]]
    [optional: master [MasterModel]]
    [optional: description '[description]']
    [optional: display '[property_name]']
    [optional: needCreatedDate true|false]
    [optional: needUpdatedDate true|false]
    [optional: creatable true|false]
    [optional: embedded true|false]
    [optional: transient true|false]
    [optional: singleton true|false]
    [optional: abstract true|false]
    properties [
        // Property definitions
    ]
    [optional: actions [...]]
    [optional: validations [...]]
    [optional: uniqueSettings [...]]
    [optional: inputs [...]]
}
```

## Property Types and Syntax

### Primitive Types
```
{
    name '[PropertyName]'
    type String|Boolean|Integer|Double|Date|Time|DateTime|File|Duration
    [optional: required true]
    [optional: unique true]
    [optional: defaultValue `[value]`]
    [optional: longText true]
    [optional: computed true]
    [optional: computation `[expression]`]
    [optional: validations [...]]
}
```

### Reference/Child/Collection Properties
```
{
    name '[PropertyName]'
    type [ModelType]
    [optional: collection true]
    [optional: child true]
    [optional: inverse true]
    [optional: inverseProperty '[property_name]']
}
```

## Collection Properties (Correct Syntax)
```
{
    name '[PropertyName]'
    type [Type]
    collection true
}
```

// Example for a collection of String subjects:
```
{
    name 'Subjects'
    type String
    collection true
}
```

// Example for a collection of another model:
```
{
    name 'Subjects'
    type Subject
    collection true
}
```

## ⚠️ Common Mistakes (Do NOT do this)

// ❌ WRONG: Do not use Array, List, or similar types for collections
```
{
    name 'Subjects'
    type Array(String)
}
{
    name 'Subjects'
    type List<String>
}
{
    name 'Subjects'
    type [String]
}
```

// ✅ CORRECT: Always use collection true
```
{
    name 'Subjects'
    type String
    collection true
}
```

**Never use Array, List, or similar types for collections. Always use `collection true` with the base type.**

## Master and Parent Usage (Correct Syntax)

// To specify a master model:
```
Model {
    name 'Student'
    master College
    parent BaseUser
    properties [
        // ...
    ]
}
```

// Example from context:
```
Model {
    package 'lead.management'
    name 'User'
    parent BaseUser
    master Company
    properties [ ... ]
    // ...
}
```

**Never use type 'reference' or similar for master. Always use the 'master' and 'parent' keywords at the top level of the model.**

## ⚠️ Common Master/Parent Mistakes (Do NOT do this)

// ❌ WRONG: Do not use a relationships block for master/parent
```
Model {
    name 'Student'
    properties [ ... ]
    relationships [
        {
            name 'College'
            type Master
            model 'College'
        }
        {
            name 'User'
            type Parent
            model 'BaseUser'
        }
    ]
}
```

// ✅ CORRECT: Use master/parent at the top level
```
Model {
    name 'Student'
    master College
    parent BaseUser
    properties [ ... ]
}
```

**Never use a relationships block for master/parent. Always use master/parent at the top level of the model.**

## Example Models

### FamilyInfo Example
```
Model {
    name 'Family Info'
    creatable false
    properties [
        {
            name 'Spouse Name'
            type String
        }
        {
            name 'Children'
            type Child
            collection true
            child true
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
            name 'has Elderly Care Responsibility'
            type Boolean
        }
        {
            name 'annisversary Date'
            type Date
        }
    ]
}
```

### Lead Example
```
Model {
    package 'lead.management'
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
        }
        {
            name 'Phone'
            type String
        }
        {
            name 'Company'
            type String
        }
        {
            name 'Status'
            type LeadStatus
            required true
        }
        {
            name 'Source'
            type String
        }
        {
            name 'Notes'
            type String
        }
        {
            name 'Current Position'
            type String
        }
        {
            name 'Industry'
            type String
        }
    ]
}
```

### LeadAssignment Example
```
Model {
    name 'Lead Assignment'
    properties [
        {
            name 'Lead'
            type Lead
            required true
        }
        {
            name 'Assigned To'
            type User
            required true
        }
        {
            name 'Assigned Date'
            type Date
        }
        {
            name 'Assigned By'
            type User
            required true
        }
        {
            name 'Is Unknown Incoming'
            type Boolean
        }
    ]
    actions [
        {
            name 'OnCreateAssignedBy'
            block ```
                this.assignedDate = Date.now();
            ```
        }
    ]
}
```

### User Example
```
Model {
    package 'lead.management'
    name 'User'
    parent BaseUser
    master Company
    properties [
        {
            name 'First Name'
            type String
            required true
        }
        {
            name 'Last Name'
            type String
            required true
        }
        {
            name 'Email'
            type String
            required true
            unique true
        }
        {
            name 'Password'
            type String
            required true
        }
        {
            name 'Phone Number'
            type String
        }
        {
            name 'Role'
            type UserRole
            required true
        }
        {
            name 'Status'
            type Boolean
            defaultValue `true`
        }
    ]
}
```

## Best Practices
- Use meaningful names for models and properties
- Always specify required fields
- Use appropriate data types
- Implement proper validations
- Use computed properties for derived values
- Leverage master-child relationships appropriately
- Add meaningful error messages for validations
- Use actions for business logic
- Consider using transient models for operations
- Implement proper access controls