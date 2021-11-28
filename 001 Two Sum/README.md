# Two Sum

[Click here](README.en.md) for English explanation.


`twoSum` fonksiyonu veri tipi `integer (int)` olan tam sayıları tutan `nums` adında bir dizi `(array)` ve veri tipi yine `integer (int)` olan bir hedef tam sayı `target` değerini parametre olarak alır. `twoSum` fonksiyonu bu dizi içerisindeki iki sayının toplam değeri hedef `(target)` değerine eşit oluyor ise bu toplanan iki sayının dizi içerisindeki endekslerini bir iki elemanlı dizi `(array)` olarak döndürmelidir.


Girdi olarak verilen dizide sadece bir çözümün var olduğunu kabul edebilirsiniz. (Birden fazla opsiyonel çözüm kümesi olmadığını varsayabiliriz. ) Bununla beraber dizinin bir ögesi (elemanı) sadece bir kez kullanılabilir. (Aynı endeks içerisindeki değerin kendisi ile toplanmaması gerekiyor.)

Geri döndürülen dizideki endekslerin sırası önemli değildir.

**Örnek 1:**


**Girdi:** `nums = [2,7,11,15], target = 9`

**Çıktı:** `[0,1]`

**Çıktı:** `Çünkü nums[0] + nums[1] == 9, bu yüzden bu iki değerin endeksleri döndürülür => [0, 1].`

<br />

**Örnek 2:**


**Girdi:** `nums = [3,2,4], target = 6`

**Çıktı:** `[1,2]`

<br />

**Örnek 3:**


**Girdi:** `nums = [3,3], target = 6`

**Çıktı:** `[0,1]`

<br/>

**Kısıtlar:**
-   `2 <= nums.length <= 104`
-   `-109  <= nums[i] <= 109`
-   `-109  <= target <= 109`
-   **Sadece tek bir geçerli cevap olmalıdır.**

