<!-- Generated on 2025-07-27T02:29:29.310760 -->
### Developer Documentation for `CbChatMatrixHandlerStaticHelpers.cs`

**Overview**

The `CbChatMatrixHandlerStaticHelpers.cs` is an internal static class within the `NCS.Core` namespace. This class encompasses a set of utility methods aimed at processing and analyzing text lines within PDF structures, particularly suited for handling chat matrix data. The functionalities include checking for token presence, comparing line contents, extracting text from blocks, and string cleaning.

**Class Structure**

- **Namespace:** `NCS.Core`
- **Class Name:** `CbChatMatrixHandlerStaticHelpers`  
  - **Modifiers:** `internal static`  

Since this class consists solely of static methods, it can be utilized without instantiating the class itself.

**Methods Documentation**

### DoesLineHaveAllIncludedTokens

**Overload:**
```csharp
internal static bool DoesLineHaveAllIncludedTokens(List<string> includedTokens, _1A1PdfLine line)
```

**Description:**  
Checks if all tokens in a provided list are present within the cells of a `_1A1PdfLine` instance. It employs dictionary caching to prevent redundant tokenization when multiple checks for the same cell context occur.

**Parameters:**
- `includedTokens`: A list of string tokens to search for within the line.
- `line`: An object representing a line from a PDF document.

**Returns:**  
Returns `true` if all provided tokens are found in the line; otherwise, returns `false`.

### AreTheLineAndParameterEqual

**Overloads:**
```csharp
internal static bool AreTheLineAndParameterEqual(string firstCell, _1A1PdfLine line)
internal static bool AreTheLineAndParameterEqual(string firstCell, string secondCell, _1A1PdfLine line)
internal static bool AreTheLineAndParameterEqual(string firstCell, string secondCell, string thirdCell, _1A1PdfLine line)
```

**Description:**  
Compares the contents of a `_1A1PdfLine` with given parameters for equality. This comparison is case-insensitive.

**Parameters:**
- `firstCell`: The primary string to compare.
- `secondCell`, `thirdCell`: Additional strings provided to compare against the line (see second overload).
- `line`: An entity representing one line from a PDF document.

The method returns `true` if:
  - The lines're perfectly matched with provided strings, disregarding case sensitivity.
  - Any cell in the line contains an exact match for the provided string(s) after tokenization and conversion to a comparable format. This comparison also ignores case.

**Returns:**  
`true` if there's a perfect case-insensitive match; otherwise, `false`.

### AreTheLineAndParameterStartsWith

**Overload:**
```csharp
internal static bool AreTheLineAndParameterStartsWith(string firstCell, _1A1PdfLine line, int radious)
```

**Description:**  
Checks if a `_1A1PdfLine` starts with the specified string within a certain length variation range (radius).

**Parameters:**
- `firstCell`: The primary string to check as a starting substring.
- `line`: An entity representing one line from a PDF document.
- `radious`: Integer specifying the acceptable character count deviation between the `firstCell` and any tokens/substrings found within `line.Text`.

This comparison ignores case sensitivity.

**Returns:**  
`true` if there exists any token or substring in the line which starts precisely with `firstCell`, allowing for variations based on `radius`. Otherwise, returns false.

### AreTheLineAndParameterEndsWith

**Overload:**
```csharp
internal static bool AreTheLineAndParameterEndsWith(string firstCell, _1A1PdfLine line, int radious)
```

**Description:**  
Similar to the `StartsWith` method but checks if a `_1A1PdfLine` ends with a specified string within an allowed length variation range (radius).

**Parameters:**
- `firstCell`: The primary string expected at the beginning.
- `line`: An entity representing one line from a PDF document.
- `radious`: Integer defining acceptable deviation in character count between the `firstCell` and tokens/substrings found within `line.Text`.

This comparison ignores case sensitivity.

**Returns:**  
`true` if there's any token or substring within the line that ends with `firstCell`, allowing for defined variations dictated by `radius`. Otherwise, returns false.

### ExtractTextFromBlock

**Overload:**
```csharp
internal static string ExtractTextFromBlock(_1A1Block block)
```

**Description:**  
Concatenates all text lines within a `_1A1Block` into a single continuous string.

**Parameters:**
- `block`: An entity representing a block (group of lines) from a PDF document.

**Returns:**  
A concatenated string containing all line texts. The contribution of each line is separated by a newline character (`\n`).

### CleanIt

**Overload:**
```csharp
internal static KeyValuePair<string, string> CleanIt(KeyValuePair<string, string> candi)
```

**Description:**  
Removes specific unwanted characters (curly braces `{}`, square brackets `[]`, and pipe symbol `|`) from both the key and value of a provided `KeyValuePair`.

**Parameters:**
- `candi`: A KeyValuePair instance requiring cleaning.

**Returns:**  
A new KeyValuePair with cleaned key and value, retaining the original order but without specified symbols.

### GetKeyValueWithKey

**Overload:**
```csharp
internal static KeyValuePair<string, string> GetKeyValueWithKey(string key, string value)
```

**Description:**  
Generates a `KeyValuePair` using provided key and value strings.

**Parameters:**
- `key`: The intended key for the KeyValuePair.
- `value`: The corresponding value to be associated with the key.

**Returns:**  
A newly created KeyValuePair incorporating the provided key-value pair.

**Dependencies**

This class depends on:
- `System.Text`
- `_1A1.Data.Extensions`
- `_1A1.Text`
- `_1A1.Data.DTOs`

These dependencies provide essential functionalities like text tokenization, string manipulation extensions, and data transfer objects related to PDF parsing structures such as `_1A1PdfLine` and `_1A1Block`.

**Conclusion**

The `CbChatMatrixHandlerStaticHelpers.cs` class is a set of utility methods intended for facilitating complex interactions around parsing, especially analyzing lines from PDF documents. These helper functions cater to precise text matching, substring verification with varying lengths, and complete text extraction—all customized for optimal handling of chat matrix style data within PDF contexts. This document serves as an authoritative guide, detailing the capabilities and usage of `CbChatMatrixHandlerStaticHelpers` for developers seeking to integrate these functionalities into their applications.
