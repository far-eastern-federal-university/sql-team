Attribute VB_Name = "Module1"
Sub ExportToAccess()
    Dim oSelect, _
        proxRng As Range
        
    Dim i As Long, j As Integer, sPath As String
    
    Dim wb As Workbook
    
    Dim ws As Worksheet
    
    Set wb = ThisWorkbook
    
    'Set ws = wb.Worksheets("")
    
    Sheet1.Activate
    
    Set oSelect = Application.InputBox("Range", , Range("A1").CurrentRegion.Address, , , , , 8)

    Dim oDAO As DAO.DBEngine, oDB As DAO.Database, oRS As DAO.Recordset
    ChDir ActiveWorkbook.Path
    sPath = Application.GetOpenFilename("Acces,*.accdb")
    If sPath = "False" Then Exit Sub

    Set oDAO = New DAO.DBEngine
    Set oDB = oDAO.OpenDatabase(sPath)
    Set oRS = oDB.OpenRecordset("Sales")

    For i = 2 To oSelect.Rows.Count
        oRS.AddNew
        For j = 1 To oSelect.Columns.Count
            oRS.Fields(j) = oSelect.Cells(i, j)
        Next j
        oRS.Update
    Next i
    oDB.Close
    
    If MsgBox("Open the table?", vbYesNo) = vbYes Then
        Dim oApp As Access.Application
        Set oApp = New Access.Application
        oApp.Visible = True
        oApp.OpenCurrentDatabase sPath
        oApp.DoCmd.OpenTable "Sales", acViewNormal, acReadOnly
        oApp.DoCmd.GoToRecord , , acLast
        DoEvents
    End If
    
End Sub


