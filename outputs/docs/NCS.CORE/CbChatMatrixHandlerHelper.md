<!-- Generated on 2025-07-27T02:25:25.254106 -->
# CbChatMatrixHandlerHelper.cs Documentation

## Overview

The `CbChatMatrixHandlerHelper.cs` file is part of the NCS.Core namespace and provides utility functions for handling chat matrix processing, specifically related to document filenames and IDs. This document outlines the purpose and usage of each method within this class.

## Namespace

```csharp
namespace NCS.Core
{
    public partial class CbChatMatrixHandler
    {
        // Methods are defined here
    }
}
```

### Methods

#### 1. GetCurrentProcessingBlock
```csharp
internal static string GetCurrentProcessingBlock(string fileName, string blockName)
```
**Description:**  
Retrieves the processing block name based on the provided file name and block name.

**Parameters:**
- `fileName`: The name of the file.
- `blockName`: The name of the processing block.

**Returns:**  
A string that combines the file name without its extension, an underscore (_), and the block name.

#### 2. GetJsonIdKey
```csharp
public static string GetJsonIdKey(string file)
```
**Description:**  
Retrieves a JSON ID key based on the provided file name by appending "_json" after the filename without its extension.

**Parameters:**
- `file`: The name of the JSON file.

**Returns:**  
A string that combines the file name without its extension, an underscore (_), and "json".

#### 3. GetDocumentIdKey
```csharp
public static string GetDocumentIdKey(string currentFileName)
```
**Description:**  
Retrieves a document ID key based on the provided current file name by appending "_DocumentId" after the filename without its extension.

**Parameters:**
- `currentFileName`: The current file's name.

**Returns:**  
A string that combines the file name without its extension, an underscore (_), and "DocumentId".

#### 4. GetFileNameBasedIdKey
```csharp
internal static string GetFileNameBasedIdKey(string fileName, string addition, string separator = "_")
```
**Description:**  
Gets a filename-based ID key by appending a specified string to the filename without its extension.

**Parameters:**
- `fileName`: The name of the file.
- `addition`: The string to append after the filename.
- `separator` (optional): The separator between the filename and the appended string. Default is "_".

**Returns:**  
A formatted string combining the file name, separator, and addition string.

#### 5. GetCurrentPdfFileName
```csharp
internal string? GetCurrentPdfFileName()
```
**Description:**  
Retrieves the current PDF file's name, either directly from a state machine or by selecting the first entry from a list of file names if no direct match is found.

**Returns:**  
The name of the current PDF file as a nullable string. If not found, it returns null.

#### 6. GetCurrentJsonFileName
```csharp
internal string? GetCurrentJsonFileName()
```
**Description:**  
Retrieves the current JSON file's name, either directly from a state machine or by selecting the first entry from a list of JSON file names if no direct match is found.

**Returns:**  
The name of the current JSON file as a nullable string. If not found, it returns null.

## Summary

The `CbChatMatrixHandlerHelper.cs` class offers several utility methods to handle chat matrix-related processes such as retrieving file names and IDs. These include getting the current processing block, JSON ID key, document ID key, filename-based ID keys, and methods for identifying the current PDF or JSON file's name using state machine operations or predefined lists.
