<!-- Generated on 2025-07-27T02:16:42.866724 -->
The `CbChatMatrixHandlerConstants.cs` file is part of the NCS.Core namespace and contains a class named `CbChatMatrixHandler`. This class defines a series of constant strings representing various function names associated with processing and managing chat matrix data. Here's an overview of the different operations handled by the constants in the `CbChatMatrixHandler` class:

### File Handling and Processing
- **ESPLITRNAVFILE**: Used for splitting NAV files.
- **EDETECTRNAVFILETYPE**: Detects the type of a NAV file.
- **ECONVERTRNAVPDFTOJSONADOBE**, **ECONVERTRNAVPDFTOJSONSPIRE**, **ECONVERTRNAVPDFTOJSONAZURE**, **ECONVERTRNAVPDFTOJSONIRONPDF**: Converts PDF files to JSON using different libraries (Adobe, Spire, Azure, IronPDF).
- **EEXTRACTPARAMETERSFROMBLOCK**, **EEXTRACTDYNAMICPARAMETERSFROMBLOCK**: Extracts parameters from blocks within PDF files.
- **EQUALIFYMODELALGOTOPBOTTOM**, **EQUALIFYMODELALGOTABLE**, **EQUALIFYMODELALGOLEFTRIGHT**, **EQUALIFYMODELALGOFREETEXT**: Describes different algorithms for qualifying models.

### Database and Bucket Operations
- **EUDPATEBLOCKINDATABASE**, **EUPDATEDATABASEWITHEXTRACTEDPARAMETER**: Updates database records with processed information.
- **EUPLOADMAINFILETOS3**, **EUPLOADSIPLITFILETOS3**, **EUPLOADJSONFILETOS3**, **EUPLOADCURRENTBLOCKTOS3**: Handles uploading files to an S3 bucket (main, split, JSON, and blocks).

### Advanced Operations
- **EDETECTBLOCKFUNCTIONA**, **EDETECTBLOCKTABLEFUNCTIONA**: Detects specific elements or tables within blocks.
- **ESTARTPARALLELWORK**: Starts parallel processing for tasks.
- **ECREATECBDOCUMENTFORMAINPDF**, **ECREATECBDOCUMENTFORSPLITPDF**: Creates database documents from PDF files (main and split).
- **EDETECTBLOCKSANDTABLES**, **EARCHIVEAFTERDETECTCORRECTION**: Detects blocks and tables, archives corrected files.
- **EDETECTSOURCEFILEVERSION**: Detects the version of a source file.

### Other Operations
- **ERENAMETHESPLITFILE**: Renames split files.
- **EDETECTCURRENTFILEPROCEDURETYPE**, **EUNSUPPORTEDPROCEDURENAME**, **EDISCARDCORRECTIONFILES**, **EARCHIVECANCELLATIONPROCEDURE**: Detects the procedure type of a file, handles unsupported procedures, discards correction files, archives cancellation procedures.
- **ECHECKIFANOTHERPROCEDURETHESAMETL**: Checks if another procedure is running in the same batch (TL).

The `FUNCTION_LIST` dictionary maps each constant string to an empty string, suggesting that each function name can be associated with additional information or behavior.

### Usage Instructions
1. Import the NCS.Core namespace into your project.
2. Use the constants defined in `CbChatMatrixHandler` to identify specific procedures or operations within your code.
3. If you need to add new operation names, ensure they are added both as a constant and an entry in the `FUNCTION_LIST`.

### Example
```csharp
using NCS.Core;

string procedureName = CbChatMatrixHandler.ESPLITRNAVFILE;
// Use this `procedureName` to trigger specific actions or logic within your application.
```

The `CbChatMatrixHandlerConstants.cs` file is essential for organizing and managing operations related to chat matrix data handling, enhancing maintainability and extendibility of the code.
