struct Rectangle {
  int w;
  int h;
  
  Rectangle(int width, int height) { w = width; h = height; }
  
  int get_width() const { return w; } 
  int get_height() const { return h; }
  int area() const { return w * h; }
  int perimeter() const { return (w+h)*2; }
  
  void set_width(int width) {
      if (0 < width and width <= 1000) { w = width; }
  }
  void set_height(int height) {
      if (0 < height and height <= 2000) { h = height; } 
  }
  
  bool is_square() const {
      if (w == h) { return true; }
      return false;
  }
};
