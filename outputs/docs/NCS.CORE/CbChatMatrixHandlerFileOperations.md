<!-- Generated on 2025-07-27T02:21:19.775320 -->
## Combined Developer Documentation for CbChatMatrixHandlerFileOperations.cs

### Overview
The `CbChatMatrixHandlerFileOperations.cs` file is part of the application responsible for document processing operations, including file splitting, renaming, and information extraction from documents such as PDFs and JSON files. The methods are tailored to extract details like source file versions and document statuses.

### Dependencies
- **Namespaces:**
  - `NCS.Data.Enums`
  - `NCS.Data.Extensions`
  - `NCS.Data.Models`
  - `Microsoft.EntityFrameworkCore`
  - `Microsoft.Extensions.Logging`
  - `_1A1.Text`
  - `_1A1.Core.Model`
  - `_1A1.Data.Enums`
  - `_1A1.Core.Enum`
  - `_1A1.CMX`
  - `_1A1.Data.DTOs`
  - `_1A1.Data.Extensions`

- **Types and Interfaces:**
  - `ChatMatrixItemFormula`
  - `PromptLogItem`
  - `State`
  - `PluginFactory`
  - `PdfConverterFactory`
  - `PdfUtility`
  - `BackgroundWorkService`
  - `CbDocument`
  - `CbDocumentsDbContext`

### Methods

1. **ExtractSourceFileVersion**
   - **Overview:** 
     Extracts the source file version from a given document.
   
   - **Parameters:**
     - `TP1`: Instance of `ChatMatrixItemFormula`
     - `debug`: List for logging debug messages
   
   - **Returns:**
     - Source file version as string or null if not found.

2. **GetCurrentProcedureFileType**
   - **Overview:** 
     Determines the current document's status (e.g., active, cancelled, reinstated).
   
   - **Parameters:**
     - `debug`: List for logging debug messages
   
   - **Returns:**
     - Enum value of type `CbDocumentStatusEnum`.

3. **ExtractDateTime**
   - **Overview:** 
     Extracts dates from provided lines and checks against expected tokens.
   
   - **Parameters:**
     - `lineTokens`: List of tokenized line texts
     - `prevLine`: Previous line object or null if first line is being processed.
     - `nextLine`: Next line object (null if not provided).

4. **GetParameterFrom**
   - **Overview:** 
     Fetches parameter values from a specified line based on the expected token in context.
   
   - **Parameters:**
     - `lineTokens`: List of tokenized line texts
     - `expectedToken`: Search token to find the wanted text.
     - `splitCount`: How many elements should be ignored after finding the desired element
     - `pluginName`: Name of plugin that can manipulate the returned value

   - **Returns:**
     - String containing desired parameter or error message.

5. **ProcessRenameFile**
   - **Overview:** 
     Renames a current split PDF file using parameters provided by ChatMatrixItemFormula.
   
   - **Parameters:**
     - `TP1`: Instance of `ChatMatrixItemFormula`
     - `debug`: List for logging debug messages
     - `overrideFileName`: An optional file name that overrides the calculated value

   - **Returns:**
     - New or updated file path name if successful or null otherwise.

6. **RenameFileAfterPreProcess**
   - **Overview:** 
     Renames file after a pre-processing step, updating internal state as well.
   
   - **Parameters:**
     - `TP1`: Instance of `ChatMatrixItemFormula`
     - `debug`: List for logging debug messages
     - `prefix`: Prefix to append or prepend to new filename

7. **SplitPdfFile**
   - **Overview:** 
     Splits a main input PDF into multiple files and updates internal state with the list of split file names.
   
   - **Parameters:**
     - `debug`: List for logging debug messages
     - `backgroundWorkdId`: Guid to identify background work task
   
   - **Returns:**
     - Dictionary containing split filenames as keys and byte arrays representing them as values.

### Additional Methods (Chunk 1)

1. **SplitFilesAsync**
   - **Description**: Splits input files into smaller parts based on certain criteria.
   - **Parameters**:
     - `List<CbDocument>? documents`: A list of documents to be split.
     - `List<PromptLogItem> debug`: A list to store debug logs during the splitting process.
     - `Guid backgroundWorkdId`: An identifier for the background work.

2. **RenameSplitPdfFile**
   - **Description**: Renames split PDF files based on provided parameters.
   - **Parameters**:
     - `List<ChatMatrixItemParameter>? parameters`: Parameters used for renaming the files.
     - `List<PromptLogItem> debug`: A list to store debug logs during the renaming process.
     - `Guid documentId`: The identifier of the document whose file is to be renamed.
     - `string? overrideName`: An optional new name for the file.

3. **GetDocumentPath**
   - Description: Two variations; one retrieves the document path based on the provided `documentId`, and another retrieves it based on the `document` object.
   - **Parameters**:
     - `Guid documentId`: The identifier of the document.
     
   or

     - `CbDocument? document`: The document object; can be null if not found in the database.

4. **GetNewFileName**
   - **Description**: Generates a new file name based on provided parameters and current file information.
   - **Parameters**:
     - `List<ChatMatrixItemParameter> parameters`: Parameters for generating the new file name.
     - `string fileName`: The original file name.

5. **GetCurrentFileProcedureName**
   - **Description**: Determines the procedure name of the current file based on JSON content.
   - **Parameters**:
     - `List<PromptLogItem> debug`: A list to store debug logs during the determination process.
     - `Guid backgroundWorkdId`: An identifier for the background work.

6. **CheckProcedureTypeWithMultipleName**
   - **Description**: Checks if any of a set of multiple names corresponds to the provided tokens.
   - **Parameters**:
     - `string enumValue`: The value to check against; should be in uppercase.
     - `List<Token> tokens`: A list of tokens to compare.

### Notes
- Asynchronous operations (`async/await`) are heavily used for file handling, requiring proper handling.
- State machines and bucket services manage and rename files.
- Debugging information is tracked through the `List<PromptLogItem>` parameters.

This documentation provides a comprehensive overview and detailed descriptions of all methods available within the CbChatMatrixHandler class in the NCS.Core namespace.
