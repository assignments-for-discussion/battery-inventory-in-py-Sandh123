
def count_batteries_by_health(present_capacities):
   healthy=[]
   exchange=[]
   failed=[]
   for  i in present_capacities :
        x=100*(i/120)
        if(x>=80):
            healthy.append(i)
        else:
            if(x<65):
                failed.append(i)
            else:
                exchange.append(i)
                
    return {
    "healthy": len(healthy),
    "exchange": len(exchange),
    "failed": len(failed)
      }


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [115, 118, 80, 95, 91, 77]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
