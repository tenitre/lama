<!-- Generated on 2025-07-27T02:26:32.775358 -->
Certainly! Below is the developer documentation for the `CbChatMatrixHandlerHumanReadableJson.cs` file, focusing on the `GetJsonObject` method.

---

# Developer Documentation: CbChatMatrixHandlerHumanReadableJson.cs

## Overview
The `CbChatMatrixHandlerHumanReadableJson.cs` file contains a class `CbChatMatrixHandler` with a static method `GetJsonObject`. This method processes airport and document data to generate a JSON object in a human-readable format using predefined classes from the `_1A1.CMX` and other namespaces.

## Class: CbChatMatrixHandler

### Methods:
#### static _1A1HumanJson GetJsonObject(List<CbAirportDTO> airports, List<CbDocumentDTO> documents)

Generates a `_1A1HumanJson` object by iterating over the provided `airports` and `documents`. This method constructs a hierarchical JSON structure reflecting the relationships between airports, document types, procedures, structures, and their parameters.

**Parameters:**
- **airports**: A list of `CbAirportDTO` objects representing various airports.
- **documents**: A list of `CbDocumentDTO` objects containing detailed information within various structures and procedures.

**Returns:**  
A `_1A1HumanJson` object representing the structured data from airports, documents, document types, procedures, structures, and parameters in a human-readable format.

## Detailed Step-by-step Process:

1. **Initialize JSON Object**: Start with creating an instance of `_1A1HumanJson`.

2. **Iterating through Airports**:
    - For each `airport` in the provided list.
    - If the airport is null, skip to the next iteration.
  
3. **Creating Airport JSON Structure`:
    - Create a new `_1A1Airport` object and set its properties.

    ```csharp
    var _1a1airport = new _1A1Airport()
    {
        Name = ((CbAirportDTO)airport).ICAO,
    };
    ```

4. **Filter and Group Documents by Airport**:
    - Retrieve all unique document types associated with the current airport.
  
5. **Iterating through Document Types**:
    - For each `documenttype` in the filtered list, create a new `_1A1DocumentType`.
  
6. **Filter and Group Procedures by Document Type and Airport**:
    - Retrieve all unique procedures associated with the document type.
  
7. **Creating Procedure JSON Structure**:
    - Create a new `_1A1ProcedureType` object for each procedure.

    ```csharp
    var _1a1procedureType = new _1A1ProcedureType()
    {
        Name = ((CbProcedureDTO)procedure).Name ?? "RNAV",
    };
    ```

8. **Filter and Group Structures by Procedure, Document Type, and Airport**:
    - Retrieve all unique structures associated with the procedure.

9. **Creating Structure JSON Structure**:
    - Create a new `_1A1Structure` object for each structure.
  
10. **Adding Parameters to Structure JSON**:
    - For each block in the document associated with the current structure, iterate through its parameters and add them to the structure's `Parameters` list.

    ```csharp
    foreach (var paramList in block.CbParameters.OrderBy(x => x.CreateDate))
    {
        _1a1structure.Parameters.Add(new _1A1Parameter() { Name = paramList.CbParameterDefinition.Name, Value = paramList.Value });
    }
    ```

11. **Appending Structures to Procedure JSON**:
    - Add each created `_1A1ProcedureType` with its associated structures to the current document type.

12. **Appending Document Types to Airport JSON**:
    - For each document type containing procedures and structures, add it to the current airport's `Documents`.

13. **Appending Airports to Main JSON Object**:
    - Add each airport JSON structure (_1A1Airport) generated to the main `_1A1HumanJson` object.

14. **Return Final JSON Object**:
    - Return the fully populated `_1A1HumanJson` instance.

---

### Summary
This method provides a comprehensive conversion from raw airport and document data into a structured JSON format, ensuring readability while preserving hierarchical relationships between various entities like airports, documents, types, procedures, structures, and parameters.
