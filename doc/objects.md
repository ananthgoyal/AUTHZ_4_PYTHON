# Objects 

## Persistent
The primary abstract super class that all persistent objects inherit from

### Class Attributes:
**createdOn**: [datetime] The datetime stamp object the object was created on; cannot be changed once object is created

**createdBy**: [int] The ID of the User object that created this object

**lastModifiedOn**: [datetime] Datetime object indicating the time stamp this object was last modified

**lastModifiedBy**: [int] The of ID of the User object that last edited this object

**version**: [int] = 0 The version number of the object

**effectiveFrom**: [date] Date object indicating the time this object is effective from

**isEnabled**: bool Whether the object is enabled; default value is True unless changed by User

**id**: int The unique ID of the object
 

### Class Methods:
**test**:

## Users

## Roles

## Permissions