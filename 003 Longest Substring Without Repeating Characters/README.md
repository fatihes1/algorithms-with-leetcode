
# Longest Substring Without Repeating Characters

[Click here](README.en.md) for English explanation.

Veri tipi **`string`** olan bir dizi verildiğinde, karakterleri tekrar etmeden elde edilebilecek en uzun alt dizinin uzunluğunu bulunuz.

**Örnek 1:**


**Girdi:** `s = "abcabcbb"`

**Çıktı:** `3`

**Açıklama:** `En uzun alt dizin "abc", uzunluğundan dolayı cevap = 3.`

<br />

**Örnek 2:**


**Girdi:** `s = "bbbbb"`

**Çıktı:** `1`

**Açıklama:** `En uzun alt dizin "b", uzunluğundan dolayı cevap = 1.`

<br />

**Örnek 3:**


**Girdi:** `s = "pwwkew"`

**Çıktı:** `3`

**Açıklama:** `En uzun alt dizin "wke", uzunluğundan dolayı cevap = 3.
"pwke" bir alt dizin değildir.`

<br/>


**Örnek 4:**


**Girdi:** `s = ""`

**Çıktı:** `0`

<br/>

**Kısıtlar:**
-   `0 <= s.length <= 5 * 104`
-   `s`  İngilizce harflerden, rakamlardan, sembollerden ve boşluklardan oluşur.



