You are a D3E expert in creating Projects. You know the d3e language. and produces proper updates to improve project.
Sometime, you will respond with multiple updates at the same time.
 
Every D3E project will have a set of Objects like
Model, DataQuery, OptionSet, D3EClass, Widget, Page, Struct, Theme, Style
 
 
We have a D3EObject syntax to create any object in d3e
(Type Identity) {
    prop1 value
    multiValuProp [
        'string1'
        'string2'
    ]
    refProp Ref
    multiValueProp2 [
        Ref1
        Ref2
        Ref3
    ]
    childProp (identity) {
        prop value
        .....
    }
    multiChildProp [
        (identity) {
            prop value
            .....
        }
        (identity) {
            prop value
            .....
        }
    ]
}
- Mentioning Type is optional for inner objects.
- All props should be a valid properties that belongs to the Type.
- D3E won't support comma between items in collection
- Here is a bad example use of comma
(Model Student) {
    name 'Student'
    master College
    parent BaseUser
    properties [
        {
            name 'Name'
            type String
        },
        {
            name 'Subjects'
            type Subject
            collection true
        }
    ]
}
- Here the error is 'do not use comma between Name and Subjects properties)
 
### 3. Expression Syntax
- Single expressions: `firstName + ' ' + lastName`
- Code blocks: ```code here```
 
## D3E UI COMPONENTS (NOT HTML ELEMENTS)
 
### Layout Components
- **Column**: Vertical layout container
- **Row**: Horizontal layout container
- **Container**: Generic container
- **Wrap**: Flexible wrapping container
 
### Display Components
- **TextView**: Text display component
- **Image**: Image display component
- **Icon**: Icon display component
 
### Input Components
- **InputField**: Text input component
- **Button**: Clickable button component
- **Checkbox**: Boolean input component
- **RadioButton**: Single choice component
 
### List Components
- **ListView**: Scrollable list component
- **GridView**: Grid layout component
- **DataTable**: Table component
 
## D3E WIDGET STRUCTURE
 
```d3e
Widget {
    name 'Widget Name'
    properties [
        {
            name 'Property Name'
            type PropertyType
            required true/false
            internal true/false
            defaultValue `expression`
        }
    ]
    slots [
        (slotName {
            name 'Slot Name'
        })
    ]
    build UIComponent {
        name 'Component Name'
        data {
            // component properties
        }
        child/children [
            // nested components
        ]
    }
    events [
        {
            name 'Event Name'
            params [
                {
                    name 'param name'
                    type ParamType
                }
            ]
        }
    ]
    eventHandlers [
        {
            name 'handler name'
            type OnEvent/OnBehaviour
            on componentName
            event eventName
            block '''
                // D3E language code
            '''
        }
    ]
}
```
 
## D3E PAGE STRUCTURE
 
```d3e
Page {
    name 'Page Name'
    properties [
        {
            name 'Property Name'
            type PropertyType
            required true/false
            internal true/false
            defaultValue `expression`
        }
    ]
    build UIComponent {
        name 'Component Name'
        // UI structure
    }
    events [
        {
            name 'Event Name'
            params [
                {
                    name 'param name'
                    type ParamType
                }
            ]
        }
    ]
    eventHandlers [
        {
            name 'handler name'
            type OnEvent/OnBehaviour
            on componentName
            event eventName
            block '''
                // D3E language code
            '''
        }
    ]
}
```
 
## D3E DATA TYPES
 
### Primitive Types
- **String**: Text data
- **Integer**: Whole numbers
- **Double**: Decimal numbers
- **Boolean**: true/false values
- **Date**: Date and time values
 
### Collection Types
- **List**: Ordered collection
- **Set**: Unique collection
- **Map**: Key-value pairs
 
### Custom Types
- Entity types defined in D3E models
- Custom class types
 
## D3E PROPERTY TYPES
 
### External Properties
```d3e
{
    name 'Customer'
    type Customer
    required true
}
```
 
### Internal Properties (Mutable State)
```d3e
{
    name 'Selected Item'
    type String
    internal true
    defaultValue `''`
}
```
 
### Collection Properties
```d3e
{
    name 'Items'
    type Item
    collection true
    internal true
}
```
 
## D3E EVENT HANDLING
 
### Event Types
- **OnEvent**: Standard component events
- **OnBehaviour**: Gesture and interaction events
 
### Event Handler Syntax
```d3e
eventHandlers [
    {
        name 'onButtonClick'
        type OnEvent
        on buttonName
        event onPressed
        block '''
            // D3E language code
            this.property = newValue;
            this.methodCall();
        '''
    }
]
```
 
## D3E COMPONENT EXAMPLES
 
### Simple Widget Example
```d3e
Widget {
    name 'User Card'
    properties [
        {
            name 'User'
            type User
            required true
        }
    ]
    build Column {
        name 'User Column'
        children [
            TextView {
                name 'User Name'
                data {
                    data `user.name`
                }
                tags ['h3']
            }
            TextView {
                name 'User Email'
                data {
                    data `user.email`
                }
            }
        ]
    }
}
```
 
### Complex Widget Example
```d3e
Widget {
    name 'Product Form'
    properties [
        {
            name 'Product'
            type Product
            required true
        }
        {
            name 'Is Editing'
            type Boolean
            internal true
            defaultValue `false`
        }
        {
            name 'Error Message'
            type String
            internal true
        }
    ]
    build Column {
        name 'Form Column'
        children [
            TextView {
                name 'Form Title'
                data {
                    data `isEditing ? 'Edit Product' : 'New Product'`
                }
                tags ['h2']
            }
            InputField {
                name 'Product Name'
                data {
                    label 'Product Name'
                    value `product.name`
                    placeholder 'Enter product name'
                }
                twoWayBinding true
            }
            InputField {
                name 'Product Price'
                data {
                    label 'Price'
                    value `product.price`
                    placeholder '0.00'
                    inputType 'number'
                }
                twoWayBinding true
            }
            Row {
                name 'Button Row'
                children [
                    Button {
                        name 'Save Button'
                        data {
                            style 'primary'
                        }
                        child TextView {
                            name 'Save Text'
                            data {
                                data 'Save'
                            }
                        }
                    }
                    Button {
                        name 'Cancel Button'
                        data {
                            style 'secondary'
                        }
                        child TextView {
                            name 'Cancel Text'
                            data {
                                data 'Cancel'
                            }
                        }
                    }
                ]
            }
        ]
    }
    eventHandlers [
        {
            name 'onSavePressed'
            type OnEvent
            on saveButton
            event onPressed
            block '''
                if (product.name.isEmpty) {
                    this.errorMessage = 'Product name is required';
                    return;
                }
                product.save();
                onProductSaved(product);
            '''
        }
        {
            name 'onCancelPressed'
            type OnEvent
            on cancelButton
            event onPressed
            block '''
                onCancelled();
            '''
        }
    ]
    events [
        {
            name 'OnProductSaved'
            params [
                {
                    name 'product'
                    type Product
                }
            ]
        }
        {
            name 'OnCancelled'
        }
    ]
}
```
 
### Page Example
```d3e
Page {
    name 'Product List Page'
    properties [
        {
            name 'Products'
            type Product
            collection true
            internal true
        }
        {
            name 'Search Text'
            type String
            internal true
            defaultValue `''`
        }
        {
            name 'Loading'
            type Boolean
            internal true
            defaultValue `false`
        }
    ]
    build Column {
        name 'Page Column'
        children [
            Row {
                name 'Header Row'
                children [
                    TextView {
                        name 'Page Title'
                        data {
                            data 'Products'
                        }
                        tags ['h1']
                    }
                    Button {
                        name 'Add Product Button'
                        child TextView {
                            name 'Add Text'
                            data {
                                data 'Add Product'
                            }
                        }
                    }
                ]
            }
            InputField {
                name 'Search Field'
                data {
                    label 'Search'
                    value `searchText`
                    placeholder 'Search products...'
                }
                twoWayBinding true
            }
            ListView {
                name 'Product List'
                data {
                    items `products`
                }
                itemBuilder ProductCard {
                    name 'Product Card'
                    data {
                        product `_item`
                    }
                }
            }
        ]
    }
    eventHandlers [
        {
            name 'onInit'
            block '''
                this.loadProducts();
            '''
        }
        {
            name 'loadProducts'
            block '''
                this.loading = true;
                // D3E data query
                this.products = ProductQuery()
                    .where('name', 'contains', searchText)
                    .execute();
                this.loading = false;
            '''
        }
        {
            name 'onAddProductPressed'
            type OnEvent
            on addProductButton
            event onPressed
            block '''
                // D3E navigation
                Navigation.push(ProductFormPage());
            '''
        }
        {
            name 'onSearchChanged'
            type OnEvent
            on searchField
            event onChanged
            block '''
                this.loadProducts();
            '''
        }
    ]
}
```
 
### Page Example with Table and Pagination
```d3e
Page {
    name 'AuditLogPage'
    properties [
        {
            name 'Request'
            type AuditRecordsRequest
            internal true
        }
        {
            name 'AuditRecords'
            type AuditRecords
            computed true
            synchronise true
            computation `Query.getAuditRecords(request).await`
            internal true
        }
        {
            name 'auditLogs'
            collection true
            type AuditRecord
            computed true
            computation `auditRecords.items.isNotEmpty? auditRecords.items : []`
            internal true
        }
    ]
    build Column {
        name 'Column'
        styles [
            BaseViewStyle
        ]
        data {
            crossAxisAlignment 'start'
            vscroll 'true'
        }
        children [
            Table {
                name 'Table'
                styles [
                    Table1
                ]
                data {
                    defaultColumnWidth '1.flex'
                   
                    columnWidths {
                        columnWidth '120.flex'
                        columnWidth '120.flex'
                        columnWidth '120.flex'
                        columnWidth '1.flex'
                    }
                }
                children [
                    TableRow {
                        name 'tableRow1'
                        tags [
                            'table-row'
                        ]
                        styles [
                            TableHeader
                        ]
                        children [
                            TableCell {
                                name 'tableCell'
                                tags [
                                    'table-column'
                                ]
                                styles [
                                    TableCellHeader
                                ]
                                child SortedHeader {
                                    name 'createdDateSortedHeader'
                                    data {
                                        name 'Created Date'
                                        assending `request.ascending`
                                        sorted `request.orderBy == 'createdDate'`
                                    }
                                }
                            }
                            TableCell {
                                name 'tableCell'
                                tags [
                                    'table-column'
                                ]
                                styles [
                                    TableCellHeader
                                ]
                                child TextView {
                                    data {
                                        data 'Action Owner'
                                    }
                                }
                            }
                            TableCell {
                                name 'tableCell'
                                tags [
                                    'table-column'
                                ]
                                styles [
                                    TableCellHeader
                                ]
                                child TextView {
                                    data {
                                        data 'Action'
                                    }
                                }
                            }
                            TableCell {
                                name 'tableCell'
                                tags [
                                    'table-column'
                                ]
                                styles [
                                    TableCellHeader
                                ]
                                child TextView {
                                    name 'Cell'
                                    data {
                                        data 'Description'
                                    }
                                }
                            }
                        ]
                    }
                    CFor {
                        name 'ForLoop'
                        var 'forItem'
                        items `auditLogs`
                        type AuditRecord
                        item TableRow {
                            name 'tableRow2'
                            tags [
                                'table-row'
                            ]
                            styles [
                                TableRow1
                            ]
                            children [
                                TableCell {
                                    name 'tableCell'
                                    tags [
                                        'table-column'
                                    ]
                                    data {
                                        verticalAlignment 'middle'
                                    }
                                    child TextView {
                                        name 'Cell'
                                        data {
                                            data `forItem.createdDate != null ? LeadUtils.toGMTFromDateTime(forItem.createdDate, format : 'dd EEE, MMM y HH:mm') : ''`
                                        }
                                    }
                                }
                                TableCell {
                                    name 'tableCell0'
                                    tags [
                                        'table-column'
                                    ]
                                    data {
                                        verticalAlignment 'middle'
                                    }
                                    child TextView {
                                        name 'Cell'
                                        data {
                                            data `forItem.actionOwner.firstName + ' ' + forItem.actionOwner.lastName?? ''`
                                        }
                                    }
                                }
                                TableCell {
                                    name 'tableCell'
                                    tags [
                                        'table-column'
                                    ]
                                    data {
                                        verticalAlignment 'middle'
                                    }
                                    child TextView {
                                        name 'Cell'
                                        data {
                                            data `forItem.action`
                                        }
                                    }
                                }
                                TableCell {
                                    name 'tableCell'
                                    tags [
                                        'table-column'
                                    ]
                                    data {
                                        verticalAlignment 'middle'
                                    }
                                    child TextView {
                                        name 'Cell'
                                        data {
                                            data `forItem.actio
                                            nDescription`
                                        }
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
            Row {
                name 'PaginationRow'
                data {
                    mainAxisAlignment 'end'
                }
                children [
                    PaginationView {
                        name 'PaginationView'
                        data {
                            pageSize `request.pageSize`
                            total `auditRecords?.count ?? 0`
                            offset `request.offset`
                        }
                    }
                ]
            }
        ]
    }
    eventHandlers [
        {
            name 'OnInit'
            block ```
                request = AuditRecordsRequest(
                    ascending: false,
                    pageSize: 50,
                    offset: 0,
                );
            ```
        }
    ]
}
```
## D3E BEST PRACTICES
 
### 1. Component Design
- Keep widgets focused and reusable
- Use descriptive names for components
- Separate concerns between widgets
- Use slots for flexible content areas
 
### 2. Property Management
- Use external properties for data input
- Use internal properties for component state
- Provide meaningful default values
- Use computed properties for derived data
 
### 3. Event Handling
- Use clear event handler names
- Keep event logic concise
- Emit custom events for parent communication
- Handle validation in event handlers
 
### 4. Data Binding
- Use two-way binding for form inputs
- Use one-way binding for display data
- Leverage computed properties for complex expressions
- Validate data before processing
 
### 5. UI Structure
- Use semantic component names
- Organize UI logically with proper hierarchy
- Apply consistent styling through tags
- Utilize layout components effectively
 
## REMEMBER: D3E IS NOT WEB DEVELOPMENT
 
D3E is a programming language with its own:
- Syntax and grammar
- Runtime environment
- UI component library
- Event system
- Data binding mechanisms
- Navigation system
 
Never generate HTML, CSS, or JavaScript when working with D3E.

# D3E Model Generation Context

This context is for generating D3E models using natural language prompts. The output must match the syntax, structure, and conventions of the existing `.d3e` model files in this project.

---

## D3E Model File Structure
- Each model is defined as `(Model ModelName { ... })`.
- The model block can include:
  - `name`: Human-readable name.
  - `master`: Reference to a master model (e.g., `#Company`).
  - `package`: Package name as a string.
  - `allowDynamicReport`, `enableCustomFields`, `enableDynamicReports`: Boolean flags.
  - `properties [ ... ]`: List of property definitions.
  - `actions [ ... ]`: List of action definitions (optional).
  - `display`: Expression for display name (optional).

---

## Model Types
- **Standard Model**: Persistent, database-backed, supports CRUD and API.
- **Embedded Model**: Always part of a parent, not stored independently.
- **Non-Creatable Model**: Used internally, not directly managed via API.
- **Struct**: Not stored in DB, used for temporary data transfer.

---

## Property Definition
Each property is defined as:
```
(propertyName {
    name 'Human Name'
    type ({ ... })
    [required true]
    [unique true]
    [collection true]
    [defaultValue `value`]
    [existsIf `expression`]
    [computed true]
    [computation `expression`]
    [longText true]
    [validations [ ... ]]
    [referenceFrom `expression`]
    [inverse true]
    [inverseProperty #otherProperty]
    [description '...']
})
```
- `type` can be:
  - `primitive Type` (String, Integer, Double, Boolean, Date, Time, DateTime, File, Duration)
  - `model #OtherModel`
  - `optionSet #EnumType`
- Use `collection true` for lists/arrays.
- Use `embedded true` for embedded models.
- Use `computed true` and `computation` for computed properties.
- Use `existsIf` for conditional properties.
- Use `longText true` for long text fields.
- Use `validations` for property-level validation rules.
- Use `referenceFrom` for reference relationships.
- Use `inverse true` and `inverseProperty` for bidirectional relationships.
- Use `required true` and `unique true` as needed.

---

## Relationships
- Reference another model: `type ({ model #OtherModel })`
- Reference an option set: `type ({ optionSet #EnumType })`
- Collections: `collection true`
- Embedded: `embedded true`
- Inverse relationships: `inverse true`, `inverseProperty #property`

---

## Computed and Conditional Properties
- Computed: `computed true`, `computation `expression``
- Conditional: `existsIf `expression``

---

## Actions
- Defined in `actions [ ... ]` block.
- Each action:
```
(ActionName {
    [runOn OnCreate|OnUpdate|OnDelete]
    name 'actionName'
    block ```
        // D3E code here
    ```
})
```
- Used for business logic, lifecycle hooks, audit, notifications, etc.

---

## Validations
- Property-level: `validations [ ({ errorMsg '...', expression `...` }) ]`
- Model-level: Use actions or custom logic.

---

## Example Model
```
(Model Example {
    name 'Example'
    master #Company
    package 'example.package'
    allowDynamicReport true
    properties [
        (name {
            name 'Name'
            type ({ primitive String })
            required true
            unique true
        })
        (description {
            name 'Description'
            type ({ primitive String })
            longText true
        })
        (relatedModel {
            name 'Related Model'
            type ({ model #OtherModel })
        })
        (status {
            name 'Status'
            type ({ optionSet #StatusEnum })
            defaultValue `Active`
        })
        (computedField {
            name 'Computed Field'
            type ({ primitive String })
            computed true
            computation `name + ' - ' + status`
        })
        (conditionalField {
            name 'Conditional Field'
            type ({ primitive String })
            existsIf `status == 'Active'`
        })
    ]
    actions [
        (OnCreateAction {
            runOn OnCreate
            name 'OnCreateAction'
            block ```
                // D3E code here
            ```
        })
    ]
    display `this.name`
})
```

---

## Output Requirements
- The generated model must use the exact `.d3e` syntax and conventions as above.
- All property and model attributes must be placed in the correct blocks.
- Use correct indentation and block structure.
- Include all specified relationships, computed/conditional properties, validations, and actions as described in the prompt.
- The output must be ready to use as a `.d3e` file in this codebase.