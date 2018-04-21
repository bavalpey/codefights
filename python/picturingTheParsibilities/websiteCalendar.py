"""
You're creating your own website for Harry Potter fans. As you all believe in magic, you're waiting for your personal letter from
Hogwarts, that will definitely arrive to you some day with a magnificent owl. To be prepared for this exciting moment you decided to
embed a calendar to your website on which you will mark the days when Hogwarts owls can bring letters.

Given a month and a year, return an HTML table representing the desired calendar. Follow the same format as provided in the example but
omit all whitespace characters (i.e. tabs, newlines and whitespaces) where it is possible, because you care about space efficiency.

Example

For month = 11 and year = 2016, the output should be

  websiteCalendar(month, year) =
  "<table border="0" cellpadding="0" cellspacing="0" class="month">
    <tr>
      <th colspan="7" class="month">November 2016</th>
    </tr>
    <tr>
      <th class="mon">Mon</th>
      <th class="tue">Tue</th>
      <th class="wed">Wed</th>
      <th class="thu">Thu</th>
      <th class="fri">Fri</th>
      <th class="sat">Sat</th>
      <th class="sun">Sun</th>
    </tr>
    <tr>
      <td class="noday">&nbsp;</td>
      <td class="tue">1</td>
      <td class="wed">2</td>
      <td class="thu">3</td>
      <td class="fri">4</td>
      <td class="sat">5</td>
      <td class="sun">6</td>
    </tr>
    <tr>
      <td class="mon">7</td>
      <td class="tue">8</td>
      <td class="wed">9</td>
      <td class="thu">10</td>
      <td class="fri">11</td>
      <td class="sat">12</td>
      <td class="sun">13</td>
    </tr>
    <tr>
      <td class="mon">14</td>
      <td class="tue">15</td>
      <td class="wed">16</td>
      <td class="thu">17</td>
      <td class="fri">18</td>
      <td class="sat">19</td>
      <td class="sun">20</td>
    </tr>
    <tr>
      <td class="mon">21</td>
      <td class="tue">22</td>
      <td class="wed">23</td>
      <td class="thu">24</td>
      <td class="fri">25</td>
      <td class="sat">26</td>
      <td class="sun">27</td>
    </tr>
    <tr>
      <td class="mon">28</td>
      <td class="tue">29</td>
      <td class="wed">30</td>
      <td class="noday">&nbsp;</td>
      <td class="noday">&nbsp;</td>
      <td class="noday">&nbsp;</td>
      <td class="noday">&nbsp;</td>
    </tr>
  </table>"
"""
import calendar
def websiteCalendar(month, year):
    return str.replace(calendar.HTMLCalendar().formatmonth(year,month),"\n","")
