# Feedme - Pwning Problem

## Overview

이문제는 fork를 이용하여 자식프로세를 생성하고 0x00~0xFF까지 size를 받고 그만큼 입력을 받는다.

## Vulnability

입력은 0xFF까지 가능하지만 입력을 받는 공간의 크기는 0x20밖에 되지 않기때문에 BOF가 발생한다. 하지만 Canary가 있기 때문에 단순한 BOF는 아니다.

프로그램을 자세히 살펴보면 fork를 이용하여 자식 프로세스를 만들고 입력을 받기 때문에 Canary는 매번 같다. 그리고 정상종료 되었을 때는 `ATE: 입력값` 이 출력되지만 Canary가 손상되어 비정상 종료 되면 출력되지 않는다.

이를 이용하여 카나리를 leak할 수 있고 ROP를 이용하여 Shell을 획득할 수 있다.