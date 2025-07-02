# Model with Conditional Properties

Prompt: "Create a [ModelName] model where [property] exists only if [condition]"
Example: "Create an EmployeeJob model where contractStartDate, contractEndDate, and contractDetails exist only if includeEmploymentContractDetails is true. These contract-related fields are only present when the job includes employment contract details."

Prompt: "Create a [ModelName] model where [property] exists only if [condition]"
Example: "Create a PayPolicy model where endDate exists only if payPeriod is SemiMonthly. The endDate property is only present for semi-monthly pay periods."

Prompt: "Create a [ModelName] model where [property] exists only if [condition]"
Example: "Create an EmployeeJob model where h1bStartDate, h1bEndDate, h1bNoticeApprovalDate, and h1bAttachments exist only if includeEmploymentH1BDetails is true. These H1B-related fields are only present when the job includes H1B details."

Prompt: "Create a [ModelName] model where [property] exists only if [condition]"
Example: "Create a PayPolicy model where roundOfNearest and roundOffToShiftTimes exist only if roundOffAttendance is true. These rounding properties are only present when attendance rounding is enabled."

Prompt: "Create a [ModelName] model where [property] exists only if [condition]"
Example: "Create an Employee model where email and password exist only if createLoginDetails is true. These login fields are only present when login details are being created."

Prompt: "Create a [ModelName] model where [property] exists only if [condition]"
Example: "Create a News model where publishedDate exists only if status is Published. The publishedDate property is only present when the news status is published."

Prompt: "Create a [ModelName] model where [property] exists only if [condition]"
Example: "Create a TravelRequest model where cashAdvanceAmount exists only if applyForCashAdvance is true. The cashAdvanceAmount property is only present when a cash advance is requested."

Prompt: "Create a [ModelName] model where [property] exists only if [condition]"
Example: "Create a Candidate model where profilePhoto exists only if a photo is uploaded. The profilePhoto property is only present when a candidate uploads a photo."

Prompt: "Create a [ModelName] model where [property] exists only if [condition]"
Example: "Create a Vacancy model where resumeRequired exists only if consetRequired is true. The resumeRequired property is only present when consent is required."

Prompt: "Create a [ModelName] model where [property] exists only if [condition]"
Example: "Create an Employee model where eSSRole, supervisorRole, and adminRole exist only if the company has those user roles defined."