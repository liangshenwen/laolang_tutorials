# 不同数据格式特点
1). AVRO:

主要为行存储  
设计的主要目标是为了满足schema evolution  
schema和数据保存在一起  

2). ORC：

面向列的存储格式  

由Hadoop中RC files 发展而来，比RC file更大的压缩比，和更快的查询速度  
Schema 存储在footer中  
不支持schema evolution  
支持事务(ACID)  
为hive而生，在许多non-hive MapReduce的大数据组件中不支持使用  
高度压缩比并包含索引  

3). Parquet：

与ORC类似，基于Google dremel
Schema 存储在footer
列式存储
高度压缩比并包含索引
相比ORC的局限性，parquet支持的大数据组件范围更广

# 如何选择不同的数据格式
考虑因素：

读写速度  
按行读多还是按列读多  
是否支持文件分割  
压缩率  
是否支持schema evolution  
# 不同数据格式最佳实践  
读取少数列可以选择面向列存储的ORC或者Parquet  
如果需要读取的列比较多，选择AVRO更优  
如果schema 变更频繁最佳选择avro  
实际上随着版本不断更新，现在parquet和orc都在一定程度上支持schema evolution，比如在最后面加列  
ORC的查询性能优于Parquet  
————————————————
版权声明：本文为CSDN博主「~shallot~」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/dylanzr/article/details/84553434