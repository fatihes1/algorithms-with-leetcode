# Median of Two Sorted Arrays

[Click here](README.en.md) for English explanation.

Sırayla **m** ve **n** boyutuna sahip iki sıralı dizi `(array)` olan `num1` ve `num2` dizileri parametre olarak alan ve bu iki diziyi birleştirerek oluşan yeni dizinin medyanını döndüren fonksiyonu kodlayınız.

Çalışma karmaşıklığı :  `O(log (m+n))` olmalıdır.

**Örnek 1:**


**Girdi:** ` nums1 = [1,3], nums2 = [2]`

**Çıktı:** `2.00000`

**Açıklama** `Birleştirilmiş dizi (array) = [1,2,3] medyan değeri 2 olur.`

<br />

**Örnek 2:**


**Girdi:** `nums1 = [1,2], nums2 = [3,4]`

**Çıktı:** `2.50000`

**Açıklama** `Birleştirilmiş dizi (array) = [1,2,3,4] medyan değeri (2 + 3) / 2 = 2.5. olur.`

<br />

**Örnek 3:**


**Girdi:** `nums1 = [0,0], nums2 = [0,0]`

**Çıktı:** `0.00000`

<br/>


**Örnek 4:**


**Girdi:** `nums1 = [], nums2 = [1]`

**Çıktı:** `1.00000`

<br/>

**Örnek 5:**


**Girdi:** `nums1 = [2], nums2 = []`

**Çıktı:** `2.00000`

<br/>

**Kısıtlar:**
-   `nums1.length == m`
-   `nums2.length == n`
-   `0 <= m <= 1000`
-   `0 <= n <= 1000`
-   `1 <= m + n <= 2000`
-   `-106  <= nums1[i], nums2[i] <= 106`



