# Widget-Context

# D3E Programming Language - Frontend Development
 
## CRITICAL: D3E IS A PROGRAMMING LANGUAGE
 
D3E is a standalone programming language like Dart, Java, or Python. It is NOT:
- HTML/CSS/JavaScript
- React/Vue/Angular
- Any web framework
- Web development
 
D3E has its own syntax, components, and runtime environment.
 
## D3E LANGUAGE SYNTAX RULES
 
### 1. Object Declaration Syntax
```d3e
ObjectType {
    name 'Object Name'
    // properties and methods
}
```
 
### 2. Collection Syntax (NO COMMAS)
```d3e
properties [
    {
        name 'Property1'
        type String
    }
    {
        name 'Property2'
        type Integer
    }
]
```
 
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