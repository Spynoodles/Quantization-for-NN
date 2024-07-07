#pragma once
#include <cstdint>


struct alignas(1) qint8 {
  using underlying = int8_t;
  int8_t val_;
  qint8() = default;
  C10_HOST_DEVICE explicit qint8(int8_t val) : val_(val) {}
};