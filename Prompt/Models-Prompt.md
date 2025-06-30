# D3E Studio Model Generation Prompt Structures

## Model Creation Prompts

### Basic Model
```
Prompt: "Create a [ModelName] model with properties [property1], [property2], ..."
Example: "Create a Student model with properties Name and Subjects"
```

### Model with Inheritance and Master
```
Prompt: "Create a [ModelName] model with master [MasterModel] and parent [ParentModel]"
Example: "Create a Student model with master College and parent BaseUser"
```

### Model with Collections
```
Prompt: "Create a [ModelName] model with [property] as a collection of [Type]"
Example: "Create a Student model with Subjects as a collection of Subject"
```

### Model with Computed or Default Properties
```
Prompt: "Create a [ModelName] model with [property] computed as [expression] or default value [value]"
Example: "Create a Customer Rating model with Rating as Double and default value 0.0"
```

### Model with Actions
```
Prompt: "Create a [ModelName] model with an action [ActionName] that runs [D3E code] on [event]"
Example: "Create a Customer Rating model with an On Create action that updates the customer's rating and saves it"
```

## Example Prompts

- Create a Student model with master College, parent BaseUser, Name as String, Subjects as a collection of Subject, and created/updated date tracking.
- Create a Customer Rating model with Customer (required), Rating (required Double), Comment (long text), Attachments (collection of DFile), and an On Create action to update the customer's rating.

## 1. Basic Model Creation

### Simple Entity Model
```
Prompt: "Create a [ModelName] model with [property1], [property2], [property3] properties"

Example: "Create a Product model with name, description, price, and category properties"
```

### Model with Specific Types
```
Prompt: "Create a [ModelName] model with [property1] as [type1], [property2] as [type2], and [property3] as [type3]"

Example: "Create a Customer model with name as String, email as String, birthDate as Date, and isActive as Boolean"
```

## 2. Model with Requirements

### Required Fields Model
```
Prompt: "Create a [ModelName] model with required fields [field1], [field2] and optional fields [field3], [field4]"

Example: "Create a User model with required fields firstName, lastName, email and optional fields phone, address"
```

### Model with Unique Constraints
```
Prompt: "Create a [ModelName] model where [property] must be unique"

Example: "Create a Product model where SKU must be unique"
```

## 3. Collection and Complex Properties

### Model with Collections
```
Prompt: "Create a [ModelName] model with [property1] as a collection of [type]"

Example: "Create a Student model with subjects as a collection of String and grades as a collection of Grade"
```

### Model with Long Text
```
Prompt: "Create a [ModelName] model with [property] as long text for detailed content"

Example: "Create a BlogPost model with content as long text for detailed content"
```

## 4. Relationship Models

### Master-Child Relationship
```
Prompt: "Create a [ChildModel] model that belongs to [MasterModel] as master"

Example: "Create an Employee model that belongs to Company as master"
```

### Reference Relationship
```
Prompt: "Create a [ModelName] model that references [ReferencedModel]"

Example: "Create an Order model that references Customer"
```

### Inverse Relationship
```
Prompt: "Create a [ModelName] model with inverse relationship to [RelatedModel] through [property]"

Example: "Create a Department model with inverse relationship to Employee through department property"
```

## 5. Computed and Conditional Properties

### Computed Properties
```
Prompt: "Create a [ModelName] model with computed [property] calculated from [expression]"

Example: "Create an Invoice model with computed totalAmount calculated from sum of line items"
```

### Conditional Properties
```
Prompt: "Create a [ModelName] model where [property] exists only if [condition]"

Example: "Create a User model where adminPrivileges exists only if role is Admin"
```

## 6. Validation Models

### Property Validations
```
Prompt: "Create a [ModelName] model with [property] validated by [validation_rule]"

Example: "Create a User model with email validated by email format and password with minimum 8 characters"
```

### Model Validations
```
Prompt: "Create a [ModelName] model with validation that [cross_field_validation]"

Example: "Create a DateRange model with validation that startDate must be before endDate"
```

## 7. Action-Based Models

### Lifecycle Actions
```
Prompt: "Create a [ModelName] model with action on [lifecycle_event] to [action_description]"

Example: "Create a User model with action on create to send welcome email"
```

### Business Logic Actions
```
Prompt: "Create a [ModelName] model with action to [business_logic] when [trigger]"

Example: "Create an Order model with action to update inventory when order is created"
```

## 8. Specialized Model Types

### Transient Models
```
Prompt: "Create a transient [ModelName] model for [purpose]"

Example: "Create a transient LoginRequest model for user authentication"
```

### Embedded Models
```
Prompt: "Create an embedded [ModelName] model for [purpose]"

Example: "Create an embedded Address model for contact information"
```

### Abstract Models
```
Prompt: "Create an abstract [ModelName] model as base for [derived_models]"

Example: "Create an abstract Person model as base for Customer and Employee models"
```

## 9. Complex Business Models

### CRM Models
```
Prompt: "Create a comprehensive [ModelName] model for CRM with [specific_requirements]"

Example: "Create a comprehensive Lead model for CRM with contact info, interaction history, and assignment tracking"
```

### E-commerce Models
```
Prompt: "Create an e-commerce [ModelName] model with [specific_features]"

Example: "Create an e-commerce Product model with variants, pricing, inventory, and reviews"
```

### Project Management Models
```
Prompt: "Create a project management [ModelName] model for [specific_purpose]"

Example: "Create a project management Task model for tracking with assignments, dependencies, and progress"
```

## 10. Integration Models

### File Handling Models
```
Prompt: "Create a [ModelName] model with file properties for [file_purpose]"

Example: "Create a Document model with file properties for PDF storage and metadata"
```

### Audit Models
```
Prompt: "Create a [ModelName] model with audit trail for [tracking_purpose]"

Example: "Create a UserActivity model with audit trail for tracking user actions"
```

## 11. Specific Syntax Prompts

### Default Values
```
Prompt: "Create a [ModelName] model with [property] having default value [value]"

Example: "Create a Task model with status having default value 'Pending'"
```

### Package Structure
```
Prompt: "Create a [ModelName] model in [package_name] package"

Example: "Create a User model in user.management package"
```

## 12. Comprehensive Model Prompts

### Full-Featured Model
```
Prompt: "Create a complete [ModelName] model for [business_domain] including [feature1], [feature2], [feature3], with validations, actions, and relationships"

Example: "Create a complete Order model for e-commerce including customer reference, order items, payment tracking, with validations, status change actions, and inventory updates"
```

### Migration from Existing Schema
```
Prompt: "Create D3E models based on this database schema: [schema_description]"

Example: "Create D3E models based on this database schema: Users table with id, name, email, and Orders table with id, user_id, total_amount"
```

## Prompt Enhancement Tips

1. **Be Specific**: Include exact property names and types
2. **Include Business Logic**: Mention validations, actions, and constraints
3. **Specify Relationships**: Clearly define how models relate to each other
4. **Mention Package**: Include package structure if relevant
5. **Include Constraints**: Specify required fields, unique constraints, etc.
6. **Add Context**: Provide business domain context for better understanding
7. **Specify Lifecycle**: Mention if you need creation/update tracking
8. **Include Access Control**: Specify if you need special permissions

## Example Complex Prompt

```
"Create a comprehensive Customer model in the crm.management package with:
- Required properties: firstName, lastName, email (unique)
- Optional properties: phone, company, address (as embedded Address model)
- Collection properties: orders (reference to Order model), tags (String collection)
- Computed property: fullName from firstName and lastName
- Conditional property: premiumBenefits that exists only if customerType is Premium
- Validation: email must be valid format
- Action on create: send welcome email and create customer record in external system
- Action on update: log changes to audit trail
- Needs created and updated date tracking
- Master-child relationship with ContactHistory model"
```

This comprehensive prompt structure will generate a fully-featured D3E model with all specified characteristics. 