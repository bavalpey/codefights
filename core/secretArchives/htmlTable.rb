=begin
HTML tables allow web developers to arrange data into rows and columns of cells. They are created using the <table> tag. Its
content consists of one or more rows denoted by the <tr> tag. Further, the content of each row comprises one or more cells
denoted by the <td> tag, and content within the <td> tags is what site visitors see in the table. For this task assume that
tags have no attributes in contrast to real world HTML.

Some tables contain the <th> tag. This tag defines header cells, which shouldn't be counted as regular cells.

You are given a rectangular HTML table. Extract the content of the cell with coordinates (row, column).



Example

  For table = "<table><tr><td>1</td><td>TWO</td></tr><tr><td>three</td><td>FoUr4</td></tr></table>", row = 0, and column = 1,
  the output should be
    htmlTable(table, row, column) = "TWO".

    <table>
     <tr>
      <td>1</td>
      <td>TWO</td>
     </tr>
     <tr>
      <td>three</td>
      <td>FoUr4</td>
     </tr>
    </table>

  corresponds to:

    1	TWO
    three	FoUr4

  For table = "<table><tr><td>1</td><td>TWO</td></tr></table>", row = 1, and column = 0, the output should be
    htmlTable(table, row, column) = "No such cell".

    <table>
     <tr>
      <td>1</td>
      <td>TWO</td>
     </tr>
    </table>
    
  corresponds to:

    1	TWO
=end


def htmlTable(table, row, column)
  pattern = /(?<=<table>)(<tr>.*?<\/tr>){#{row}}<tr>(?:<th>|<\/th>|\w)*?(<td>\w*<\/td>){#{column}}<td>(.*?)<\/td>/
  begin
    return pattern.match(table)[3]
  rescue
    return "No such cell"
  end
end
