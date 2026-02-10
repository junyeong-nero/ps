# "왜 미리 사두지 않나요?" (질문에 대한 답변)
# **"어차피 나중에 사도 가격(코인)은 똑같고, 오히려 선택지는 넓어지기 때문"**입니다.
#     코인 보존: 1라운드에 미리 코인을 써버리면, 나중에 코인 없이도 넘길 수 있는 '공짜 쌍'이 나왔을 때 대응할 코인이 부족해질 수 있습니다.
#     유연성 확보: 보관소에 넣어두는 행위는 **"언제든 꺼내 쓸 수 있는 냉장고"**에 음식을 보관하는 것과 같습니다. 미리 꺼내서(코인 지불) 상온에 둘(내 손으로 가져올) 필요가 전혀 없습니다.
#     최적해 보장: 이 방식은 현재 가능한 가장 저렴한 비용으로 라운드를 돌파하게 하므로 그리디하게 최적의 결과를 보장합니다.

def solution(coin, cards):
    n = len(cards)
    hand = set(cards[:n//3])  # 처음에 가진 카드
    pending = set()           # 라운드를 진행하며 뽑았지만 아직 코인을 안 쓴 카드
    
    current_idx = n // 3
    round_count = 1
    
    # 두 집합(s1, s2)에서 합이 n+1이 되는 쌍이 있는지 찾고 제거하는 함수
    def find_pair(s1, s2):
        nonlocal coin
        for card in list(s1):
            target = (n + 1) - card
            if target in s2:
                # s1과 s2가 같은 집합일 경우를 대비해 target 존재를 먼저 체크
                # 실제 문제 로직상:
                # 1. hand & hand -> 0개
                # 2. hand & pending -> 1개
                # 3. pending & pending -> 2개
                
                # 하지만 이 함수는 호출 순서에 의해 자동으로 코인 개수가 결정됨
                return True, card, target
        return False, None, None

    while current_idx < n:
        # 1. 카드 2장 뽑아서 보관소에 넣기
        pending.add(cards[current_idx])
        pending.add(cards[current_idx + 1])
        current_idx += 2
        
        # 2. 다음 라운드로 갈 수 있는지 우선순위에 따라 체크
        # 우선순위 1: 내 손안의 카드끼리 (코인 0개)
        found, c1, c2 = find_pair(hand, hand)
        if found:
            hand.remove(c1)
            hand.remove(c2)
            round_count += 1
            continue
            
        # 우선순위 2: 내 손의 카드 1장 + 보관소 카드 1장 (코인 1개)
        if coin >= 1:
            found, c1, c2 = find_pair(hand, pending)
            if found:
                hand.remove(c1)
                pending.remove(c2)
                coin -= 1
                round_count += 1
                continue
                
        # 우선순위 3: 보관소 카드 2장 (코인 2개)
        if coin >= 2:
            found, c1, c2 = find_pair(pending, pending)
            if found:
                pending.remove(c1)
                pending.remove(c2)
                coin -= 2
                round_count += 1
                continue
        
        # 어떤 경우로도 라운드를 넘길 수 없으면 종료
        break
        
    return round_count
