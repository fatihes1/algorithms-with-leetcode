
##### [Click here](https://github.com/ErdalNayir/algorithms-with-leetcode/blob/main/005%20Remove%20Nth%20Node%20From%20End%20of%20List/README.en.md) for english explanation
Verilen bağlı listeden, sondan n'inci elemanı silin ve yeni bağlı listenin baş kısmını döndürün.

#### Resim:
<img src="https://github.com/ErdalNayir/algorithms-with-leetcode/blob/main/005%20Remove%20Nth%20Node%20From%20End%20of%20List/remove_ex1.jpg" alt="exampleImg" width="500" height="300" hspace="50">

 

#### Örnek 1:

Girdi: baş = [1,2,3,4,5], n = 2
Çıktı: [1,2,3,5]

#### Örnek 2:

Girdi: baş = [1], n = 1
Çıktı: []

#### Örnek  3:

Girdi: baş = [1,2], n = 1
Çıktı: [1]
 

### Kısıtlamalar:

Liste içindeki düğüm sayısı sz'dir
1 <= sz <= 30
0 <= Düğüm.val <= 100
1 <= n <= sz
