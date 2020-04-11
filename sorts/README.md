# 各种经典的排序算法  

|   **排序算法**   |    **平均时间复杂度**     |    **最好时间复杂度**     |    **最坏时间复杂度**     | **空间复杂度** | **稳定性** |
| :----------: | :-------------------: | :-------------------: | :-------------------: | :--------: | :----: |
| **直接插入排序** | $O\left(n^{2}\right)$ |        $O(n)$         | $O\left(n^{2}\right)$ |    $O(1)$    |  稳定  |
|   **希尔排序**   | $O\left(n^{1.3-2}\right)$ |        $O(n)$         | $O\left(n^{2}\right)$ |    $O(1)$    | 不稳定 |
|   **选择排序**   | $O\left(n^{2}\right)$ | $O\left(n^{2}\right)$ | $O\left(n^{2}\right)$ |    $O(1)$    | 不稳定 |
|    **堆排序**    | $O\left(\mathrm{nlog}_{2} \mathrm{n}\right)$ | $O\left(\mathrm{nlog}_{2} \mathrm{n}\right)$ | $O\left(\mathrm{nlog}_{2} \mathrm{n}\right)$ |    $O(1)$    | 不稳定 |
|   **冒泡排序**   | $O\left(n^{2}\right)$ |        $O(n)$         | $O\left(n^{2}\right)$ |    $O(1)$    |  稳定  |
|   **快速排序**   | $O\left(\mathrm{nlog}_{2} \mathrm{n}\right)$ | $O\left(\mathrm{nlog}_{2} \mathrm{n}\right)$ | $O\left(n^{2}\right)$ | $O\left(\mathrm{log}_{2} \mathrm{n}\right)$ | 不稳定 |
|   **归并排序**   | $O\left(\mathrm{nlog}_{2} \mathrm{n}\right)$ | $O\left(\mathrm{nlog}_{2} \mathrm{n}\right)$ | $O\left(\mathrm{nlog}_{2} \mathrm{n}\right)$ |   $O(n)$   |  稳定  |
|   **基数排序**   | $O(d(r+n))$ | $O(d(n+rd))$ | $O(d(r+n))$ | $O(rd+n)$ |  稳定  |

> 在**基数排序**中，`d`代表其排序中最大数的位数，`r`代表基数，`n`代表排序的个数。