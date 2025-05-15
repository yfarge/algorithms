#include <unordered_map>

using namespace std;

class ParkingSystem {
private:
  unordered_map<int, int> count;

public:
  ParkingSystem(int big, int medium, int small) {
    count[1] = big;
    count[2] = medium;
    count[3] = small;
  }

  bool addCar(int carType) { return --count[carType] >= 0; }
};

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem* obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj->addCar(carType);
 */
