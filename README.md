**Author/Beta-TNT**

As a classic string/sequence matching algorithm, I believe every reader who is graduated from computer science college knows "KMP". But every examples you can find on the Internet are just boring codes, matching a certain given target string. One of the advantages of KMP algorithm is that there is no need to "watch back", so, indeed KMP is capable for not just fixed or certain given target string/sequence, but also an unlimited one. In the field of Network Security, we often need to check whether a certain subsequence or sequence fragment matches a ruleset, the KMP is perfect for this situation. The implementation is quite simple: all we need is a queue which has a max length that equals to the length of pattern string, we use this queue as a "window". When mismatch happens, the window slides to right, which means append new char to the rear, if the window reached its maximum length, it will pop first char automatically. We check the window's contents only when it is full.

<table>

<tbody>

<tr>

<td colspan="4"></td>

<td style="text-align: center;" colspan="5" bgcolor="Silver">Window</td>

<td colspan="2"></td>

</tr>

<tr>

<td>Target</td>

<td style="text-align: center;">…</td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;" bgcolor="Yellow">a</td>

<td style="text-align: center;" bgcolor="Yellow">b</td>

<td style="text-align: center;" bgcolor="Yellow">a</td>

<td style="text-align: center;" bgcolor="Yellow">b</td>

<td style="text-align: center;" bgcolor="Yellow">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">…</td>

</tr>

<tr>

<td>Pattern</td>

<td style="text-align: center;"></td>

<td style="text-align: center;"></td>

<td style="text-align: center;"></td>

<td style="text-align: center;" bgcolor="Yellow">a</td>

<td style="text-align: center;" bgcolor="Yellow">b</td>

<td style="text-align: center;" bgcolor="Yellow">a</td>

<td style="text-align: center;" bgcolor="Yellow">b</td>

<td style="text-align: center;" bgcolor="Yellow">b</td>

<td style="text-align: center;"></td>

<td style="text-align: center;"></td>

</tr>

</tbody>

</table>

If you don't want KMP thing, check all the contents every time when it slides, that's the way Brute Force matching applied to an unlimited sequence. The KMP way is sliding a distance of mismatch index (we call it [i]) of pattern string minus next[i] (i - next[i]), and matching the pattern from the index of next[i] next time when the window is filled. Here is an example:

<table><caption>Pattern string and its NEXT array</caption>

<tbody>

<tr>

<td>Index</td>

<td style="text-align: center;">0</td>

<td style="text-align: center;">1</td>

<td style="text-align: center;">2</td>

<td style="text-align: center;">3</td>

<td style="text-align: center;">4</td>

</tr>

<tr>

<td>Pattern</td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">b</td>

</tr>

<tr>

<td>Next</td>

<td style="text-align: center;">0</td>

<td style="text-align: center;">0</td>

<td style="text-align: center;">0</td>

<td style="text-align: center;">1</td>

<td style="text-align: center;">2</td>

</tr>

</tbody>

</table>

<table><caption>Initial status</caption>

<tbody>

<tr>

<td></td>

<td style="text-align: center;" colspan="5" bgcolor="Silver">Window</td>

<td colspan="9"></td>

</tr>

<tr>

<td>Target</td>

<td></td>

<td></td>

<td></td>

<td></td>

<td></td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">b</td>

</tr>

<tr>

<td>Pattern</td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">b</td>

<td colspan="9"></td>

</tr>

<tr>

<td>Next</td>

<td style="text-align: center;">0</td>

<td style="text-align: center;">0</td>

<td style="text-align: center;">0</td>

<td style="text-align: center;">1</td>

<td style="text-align: center;">2</td>

<td colspan="9"></td>

</tr>

<tr>

<td>Index</td>

<td style="text-align: center;">0</td>

<td style="text-align: center;">1</td>

<td style="text-align: center;">2</td>

<td style="text-align: center;">3</td>

<td style="text-align: center;">4</td>

<td colspan="9"></td>

</tr>

</tbody>

</table>

<table><caption>Enqueue new char, filling the window</caption>

<tbody>

<tr>

<td></td>

<td style="text-align: center;" colspan="5" bgcolor="Silver">Window</td>

<td colspan="6"></td>

</tr>

<tr>

<td>Target</td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">a</td>

<td style="text-align: center;"></td>

<td style="text-align: center;"></td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">b</td>

</tr>

<tr>

<td>Pattern</td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">b</td>

<td colspan="6"></td>

</tr>

<tr>

<td>Next</td>

<td style="text-align: center;">0</td>

<td style="text-align: center;">0</td>

<td style="text-align: center;">0</td>

<td style="text-align: center;">1</td>

<td style="text-align: center;">2</td>

<td colspan="6"></td>

</tr>

<tr>

<td>Index</td>

<td style="text-align: center;">0</td>

<td style="text-align: center;">1</td>

<td style="text-align: center;">2</td>

<td style="text-align: center;">3</td>

<td style="text-align: center;">4</td>

<td colspan="6"></td>

</tr>

</tbody>

</table>

<table><caption>Window filled, matching starts</caption>

<tbody>

<tr>

<td></td>

<td style="text-align: center;" colspan="5" bgcolor="Silver">Window</td>

<td colspan="4"></td>

</tr>

<tr>

<td>Target</td>

<td style="text-align: center;" bgcolor="Aqua">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">b</td>

</tr>

<tr>

<td>Pattern</td>

<td style="text-align: center;" bgcolor="Aqua">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">b</td>

<td colspan="4"></td>

</tr>

<tr>

<td>Next</td>

<td style="text-align: center;" bgcolor="Aqua">0</td>

<td style="text-align: center;">0</td>

<td style="text-align: center;">0</td>

<td style="text-align: center;">1</td>

<td style="text-align: center;">2</td>

<td colspan="4"></td>

</tr>

<tr>

<td>Index</td>

<td style="text-align: center;" bgcolor="Aqua">0</td>

<td style="text-align: center;">1</td>

<td style="text-align: center;">2</td>

<td style="text-align: center;">3</td>

<td style="text-align: center;">4</td>

<td colspan="4"></td>

</tr>

</tbody>

</table>

<table><caption>First mismatch</caption>

<tbody>

<tr>

<td></td>

<td style="text-align: center;" colspan="5" bgcolor="Silver">Window</td>

<td colspan="4"></td>

</tr>

<tr>

<td>Target</td>

<td style="text-align: center;" bgcolor="Lime">a</td>

<td style="text-align: center;" bgcolor="Lime">b</td>

<td style="text-align: center;" bgcolor="Lime">a</td>

<td style="text-align: center;" bgcolor="Lime">b</td>

<td style="text-align: center;" bgcolor="Yellow">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">b</td>

</tr>

<tr>

<td>Pattern</td>

<td style="text-align: center;" bgcolor="Lime">a</td>

<td style="text-align: center;" bgcolor="Lime">b</td>

<td style="text-align: center;" bgcolor="Lime">a</td>

<td style="text-align: center;" bgcolor="Lime">b</td>

<td style="text-align: center;" bgcolor="Yellow">b</td>

<td colspan="4"></td>

</tr>

<tr>

<td>Next</td>

<td style="text-align: center;">0</td>

<td style="text-align: center;">0</td>

<td style="text-align: center;">0</td>

<td style="text-align: center;">1</td>

<td style="text-align: center;" bgcolor="Yellow">2</td>

<td colspan="4"></td>

</tr>

<tr>

<td>Index</td>

<td style="text-align: center;">0</td>

<td style="text-align: center;">1</td>

<td style="text-align: center;">2</td>

<td style="text-align: center;">3</td>

<td style="text-align: center;" bgcolor="Yellow">4</td>

<td colspan="4"></td>

</tr>

</tbody>

</table>

<table><caption>Dequeue char count (sliding distance)= Index-Next[Index] = 4 - 2 = 2</caption>

<tbody>

<tr>

<td colspan="3"></td>

<td style="text-align: center;" colspan="5" bgcolor="Silver">Window</td>

<td colspan="4"></td>

</tr>

<tr>

<td>Target</td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td>a</td>

<td></td>

<td style="text-align: center;"></td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">b</td>

</tr>

<tr>

<td>Pattern</td>

<td colspan="2"></td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">b</td>

<td colspan="4"></td>

</tr>

<tr>

<td>Next</td>

<td colspan="2"></td>

<td style="text-align: center;">0</td>

<td style="text-align: center;">0</td>

<td style="text-align: center;">0</td>

<td style="text-align: center;">1</td>

<td style="text-align: center;">2</td>

<td colspan="4"></td>

</tr>

<tr>

<td>Index</td>

<td colspan="2"></td>

<td style="text-align: center;">0</td>

<td style="text-align: center;">1</td>

<td style="text-align: center;">2</td>

<td style="text-align: center;">3</td>

<td style="text-align: center;">4</td>

<td colspan="4"></td>

</tr>

</tbody>

</table>

<table><caption>Continue enqueue new char until the window is filled, then start matching from: Next[Index] = 2</caption>

<tbody>

<tr>

<td colspan="3"></td>

<td style="text-align: center;" colspan="5" bgcolor="Silver">Window</td>

<td colspan="2"></td>

</tr>

<tr>

<td>Target</td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;" bgcolor="Aqua">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">b</td>

</tr>

<tr>

<td>Pattern</td>

<td colspan="2"></td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;" bgcolor="Aqua">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">b</td>

<td colspan="2"></td>

</tr>

<tr>

<td>Next</td>

<td colspan="2"></td>

<td style="text-align: center;">0</td>

<td style="text-align: center;">0</td>

<td style="text-align: center;" bgcolor="Aqua">0</td>

<td style="text-align: center;">1</td>

<td style="text-align: center;">2</td>

<td colspan="2"></td>

</tr>

<tr>

<td>Index</td>

<td colspan="2"></td>

<td style="text-align: center;">0</td>

<td style="text-align: center;">1</td>

<td style="text-align: center;" bgcolor="Aqua">2</td>

<td style="text-align: center;">3</td>

<td style="text-align: center;">4</td>

<td colspan="2"></td>

</tr>

</tbody>

</table>

<table><caption>Second mismatch</caption>

<tbody>

<tr>

<td colspan="3"></td>

<td style="text-align: center;" colspan="5" bgcolor="Silver">Window</td>

<td colspan="2"></td>

</tr>

<tr>

<td>Target</td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;" bgcolor="Lime">a</td>

<td style="text-align: center;" bgcolor="Lime">b</td>

<td style="text-align: center;" bgcolor="Yellow">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">b</td>

</tr>

<tr>

<td>Pattern</td>

<td colspan="2"></td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;" bgcolor="Lime">a</td>

<td style="text-align: center;" bgcolor="Lime">b</td>

<td style="text-align: center;" bgcolor="Yellow">b</td>

<td colspan="2"></td>

</tr>

<tr>

<td>Next</td>

<td colspan="2"></td>

<td style="text-align: center;">0</td>

<td style="text-align: center;">0</td>

<td style="text-align: center;">0</td>

<td style="text-align: center;">1</td>

<td style="text-align: center;" bgcolor="Yellow">2</td>

<td colspan="2"></td>

</tr>

<tr>

<td>Index</td>

<td colspan="2"></td>

<td style="text-align: center;">0</td>

<td style="text-align: center;">1</td>

<td style="text-align: center;">2</td>

<td style="text-align: center;">3</td>

<td style="text-align: center;" bgcolor="Yellow">4</td>

<td colspan="2"></td>

</tr>

</tbody>

</table>

<table><caption>Sliding distance = Index-Next[Index] = 4 - 2 = 2 Start matching from = Next[Index] = 2</caption>

<tbody>

<tr>

<td colspan="5"></td>

<td style="text-align: center;" colspan="5" bgcolor="Silver">Window</td>

</tr>

<tr>

<td>Target</td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;" bgcolor="Aqua">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">b</td>

</tr>

<tr>

<td>Pattern</td>

<td colspan="4"></td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;" bgcolor="Aqua">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">b</td>

</tr>

<tr>

<td>Next</td>

<td colspan="4"></td>

<td style="text-align: center;">0</td>

<td style="text-align: center;">0</td>

<td style="text-align: center;" bgcolor="Aqua">0</td>

<td style="text-align: center;">1</td>

<td style="text-align: center;">2</td>

</tr>

<tr>

<td>Index</td>

<td colspan="4"></td>

<td style="text-align: center;">0</td>

<td style="text-align: center;">1</td>

<td style="text-align: center;" bgcolor="Aqua">2</td>

<td style="text-align: center;">3</td>

<td style="text-align: center;">4</td>

</tr>

</tbody>

</table>

<table><caption>Finally matched</caption>

<tbody>

<tr>

<td colspan="5"></td>

<td style="text-align: center;" colspan="5" bgcolor="Silver">Window</td>

</tr>

<tr>

<td>Target</td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;" bgcolor="Lime">a</td>

<td style="text-align: center;" bgcolor="Lime">b</td>

<td style="text-align: center;" bgcolor="Lime">b</td>

</tr>

<tr>

<td>Pattern</td>

<td colspan="4"></td>

<td style="text-align: center;">a</td>

<td style="text-align: center;">b</td>

<td style="text-align: center;" bgcolor="Lime">a</td>

<td style="text-align: center;" bgcolor="Lime">b</td>

<td style="text-align: center;" bgcolor="Lime">b</td>

</tr>

<tr>

<td>Next</td>

<td colspan="4"></td>

<td style="text-align: center;">0</td>

<td style="text-align: center;">0</td>

<td style="text-align: center;">0</td>

<td style="text-align: center;">1</td>

<td style="text-align: center;" bgcolor="Lime">2</td>

</tr>

<tr>

<td>Index</td>

<td colspan="4"></td>

<td style="text-align: center;">0</td>

<td style="text-align: center;">1</td>

<td style="text-align: center;">2</td>

<td style="text-align: center;">3</td>

<td style="text-align: center;" bgcolor="Lime">4</td>

</tr>

</tbody>

</table>

As the way how to match an unlimited sequence, I use the "feed data" mechanism. If the window slides a length longer than 2 chars, matching will not begin until the window is filled. The feed data function will return None if the sequence doesn't meet the pattern, or "i" pointer (index of the begin of matched subsequence) and window content if matches.
