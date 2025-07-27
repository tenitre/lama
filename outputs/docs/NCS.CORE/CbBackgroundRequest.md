<!-- Generated on 2025-07-27T02:13:11.317551 -->
# Developer Documentation: CbBackgroundRequest.cs

## Overview

`CbBackgroundRequest.cs` is a C# file located in the `NCS.Core.BackgroundWork` namespace. This file contains the definition of the `CbBackgroundRequest` class, which serves as a model for background request data structures within an application.

## Class Definition

### Namespace
- **Namespace:** NCS.Core.BackgroundWork

### Class: CbBackgroundRequest
The `CbBackgroundRequest` class is designed to encapsulate information related to background requests. It includes various properties that facilitate the management and tracking of these requests.

#### Properties:

1. **CbDatabaseId**
   - **Type:** Guid
   - **Accessors:** get, set
   - **Description:** A unique identifier for the database related to the background request.
   - **Example:**
     ```csharp
     var requestId = new CbBackgroundRequest();
     requestId.CbDatabaseId = Guid.NewGuid();
     ```

2. **CbDocuments**
   - **Type:** List<Guid>
   - **Accessors:** get, set
   - **Default Value:** `new List<Guid>();`
   - **Description:** A list of unique identifiers for documents associated with the background request.
   - **Example:**
     ```csharp
     var requestId = new CbBackgroundRequest();
     requestId.CbDocuments.Add(Guid.NewGuid());
     ```

3. **CbDocumentParentBackgroundWorkId**
   - **Type:** Guid
   - **Accessors:** get, set
   - **Description:** The unique identifier of the parent background work associated with a document.
   - **Example:**
     ```csharp
     var requestId = new CbBackgroundRequest();
     requestId.CbDocumentParentBackgroundWorkId = Guid.NewGuid();
     ```

4. **CbVersionId**
   - **Type:** Guid
   - **Accessors:** get, set
   - **Description:** A unique identifier for the version of the background request.
   - **Example:**
     ```csharp
     var requestId = new CbBackgroundRequest();
     requestId.CbVersionId = Guid.NewGuid();
     ```

5. **IsAdminProcess**
   - **Type:** bool
   - **Accessors:** get, set
   - **Default Value:** `false`
   - **Description:** Indicates whether the background request process is an admin-level operation.
   - **Example:**
     ```csharp
     var requestId = new CbBackgroundRequest();
     requestId.IsAdminProcess = true;
     ```

6. **BackgroundWorks**
   - **Type:** Dictionary<Guid, Guid>
   - **Accessors:** get, set
   - **Default Value:** `new Dictionary<Guid, Guid>();`
   - **Description:** A dictionary representing background work tasks where the key is a task ID and the value is another identifier.
   - **Example:**
     ```csharp
     var requestId = new CbBackgroundRequest();
     requestId.BackgroundWorks.Add(Guid.NewGuid(), Guid.NewGuid());
     ```

## Usage Example

Here's an example of how you might use the `CbBackgroundRequest` class in a program:

```csharp
using NCS.Core.BackgroundWork;

public class Program
{
    public static void Main()
    {
        var request = new CbBackgroundRequest();
        
        request.CbDatabaseId = Guid.NewGuid();
        request.CbDocuments.Add(Guid.NewGuid());
        request.CbDocumentParentBackgroundWorkId = Guid.NewGuid();
        request.CbVersionId = Guid.NewGuid();
        request.IsAdminProcess = true;
        request.BackgroundWorks.Add(
            Guid.NewGuid(),
            Guid.NewGuid()
        );

        // Use the request object for further processing
    }
}
```

## Licensing & Copyright

`CbBackgroundRequest.cs` is part of an application developed under Alibaba Cloud. The usage and distribution are controlled by the respective service agreements or licensing terms provided by Alibaba Cloud.

---

Ensure that you understand and adhere to any additional policies or guidelines regarding the use of this code within your environment or project.

For more information, please refer to the official documentation provided with your specific application or visit the [Alibaba Cloud Documentation](https://www.alibabacloud.com-help).
