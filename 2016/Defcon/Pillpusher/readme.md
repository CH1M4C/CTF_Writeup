#Pillpusher - Pwning Problem

##Overview

이문제는 약국을 컨셉으로 하고 있는것 같다.<br>
취약점은 매우 간단한데에 비해 stripped,statically linked 되있고 바이너리는 쓸대없이 크고 복잡하다.
##Vulnability
취약점은 Scrip Menu의 Add Scrip에서 발생하게 된다.<br>
Add Scrip에서 Add pill을 할 수 있는데 2개 이상이면 무조건 2개가 되게 되있지만 signed이기 때문에 -1을 넣게 되면 무한정 넣을 수 있다.
```c
v15 = (signed int)readNum(rbp0, 0);
if ( v15 > 2 )
  size = 2LL;
else
  size = v15;
```

그렇기 때문에 pill name을  stack에 마음것 넣을 수 있게 되어 BOF를 이용해 exploit할 수 있다.

