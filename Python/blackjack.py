def blackjack_hand_greater_than(hand_1, hand_2):
      count1 = 0
      count2 = 0
###################
      for i in hand_1:
        #print (i)
            if i == 'J'or i == 'K' or i == 'Q':
                  count1 = count1 + 10
                  continue
            if i == 'A':
                  count1 = count1 + 11 
                  continue 
            else:
                  count1 = count1 + int(i)        
      print ('set 1 done')
########################    
      for i in hand_2:
        #print (i)
            if i == 'J'or i == 'K' or i == 'Q':
                  count2 = count2 + 10
                  continue
            if i == 'A':
                  count2 = count2 + 11      
                  continue 
            else:
                  count2 = count2 + int(i) 
      print ('set 2 done')
#################################      
      for i in hand_1:
            if count1 > 21 and i == 'A':
                  count1 = count1 - 10
                  #print (count1)
###################
      for i in hand_2:
            if count2 > 21 and i == 'A':
                  count2 = count2 - 10
                  #print (count2)
      print (count1, count2)
############################
      if count1 <= 21:
            if count2 <= 21:
                  if count1 > count2:
                        print ('set1')
                        return True
                  else:
                        print ('set2')
                        return False
            else:
                  print ('set1')
                  return True
      else:
            print ('wrong')
            return False

blackjack_hand_greater_than([2, 1, 'K', 'A', 5, 'A'], [8, 9])