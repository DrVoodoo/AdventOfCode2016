void main() {
  var x = "L4, R2, R4, L5, L3, L1, R4, R5, R1, R3, L3, L2, L2, R5, R1, L1, L2, R2, R2, L5, R5, R5, L2, R1, R2, L2, L4, L1, R5, R2, R1, R1, L2, L3, R2, L5, L186, L5, L3, R3, L5, R4, R2, L5, R1, R4, L1, L3, R3, R1, L1, R4, R2, L1, L4, R5, L1, R50, L4, R3, R78, R4, R2, L4, R3, L4, R4, L1, R5, L4, R1, L2, R3, L2, R5, R5, L4, L1, L2, R185, L5, R2, R1, L3, R4, L5, R2, R4, L3, R4, L2, L5, R1, R2, L2, L1, L2, R2, L2, R1, L5, L3, L4, L3, L4, L2, L5, L5, R2, L3, L4, R4, R4, R5, L4, L2, R4, L5, R3, R1, L1, R3, L2, R2, R1, R5, L4, R5, L3, R2, R3, R1, R4, L4, R1, R3, L5, L1, L3, R2, R1, R4, L4, R3, L3, R3, R2, L3, L3, R4, L2, R4, L3, L4, R5, R1, L1, R5, R3, R1, R3, R4, L1, R4, R3, R1, L5, L5, L4, R4, R3, L2, R1, R5, L3, R4, R5, L4, L5, R2";
  
  var y = x.replaceAll(" ", "");
  var z = y.split(",");
  var direction = "N";
  var directionList = new List<Direction>();

  for (int i = 0; i < z.length; i++) {
    var next_dir = z[i][0];
    var number = int.parse(z[i].substring(1));
    var newDirection = new Direction();

    var newStart = new Coordinate();
    if (directionList.length > 0){
      newStart = directionList.elementAt(directionList.length-1).end;
    } else {
      newStart.x = 0;
      newStart.y = 0;
    }

    var nextDirection = getNextDirection(direction, next_dir);    
    var newEnd = getNewEnd(newStart, nextDirection, number);
    direction = nextDirection;
           
    newDirection.start = newStart;
    newDirection.end = newEnd;
    newDirection.mapDirection = direction;

    directionList.add(newDirection);
  }
  
  print(directionList[directionList.length-1].end.x);
  print(directionList[directionList.length-1].end.y);

  // find first crossing
  var found = false;
  var crossing;
  for (int i = 0; i < directionList.length && !found; i++){
    for (int j = 0; j < i && !found; j++){
      crossing = new IsCrossing(directionList[i], directionList[j]);
      if (crossing.hasCrossing){
        found = true;
      }
    }
  }
}

String getNextDirection(direction, next_dir){
  if (direction == "N"){
      if (next_dir == "R"){
        return "E";
      } else {
        return "W";
      }
    }
    else if (direction == "S"){
      if (next_dir == "R"){
        return "W";
      } else {
        return "E";
      }
    }
    else if (direction == "E"){
      if (next_dir == "R"){
        return "S";
      } else {
        return "N";
      }
    }    
    else if (direction == "W"){
      if (next_dir == "R"){
        return "N";
      } else {
        return "S";
      }
    }
    return ""; // fix
}

Coordinate getNewEnd(newStart, direction, number){
  var newEnd = new Coordinate();
  if (direction == "N"){
    newEnd.x = newStart.x;
    newEnd.y = newStart.y + number;
  }
  else if (direction == "E"){
    newEnd.x = newStart.x + number;
    newEnd.y = newStart.y;
  }
  else if (direction == "S"){
    newEnd.x = newStart.x;
    newEnd.y = newStart.y - number;
  }
  else { // direction == "W"
    newEnd.x = newStart.x - number;
    newEnd.y = newStart.y;
  }
  return newEnd;
}

class IsCrossing {
  bool hasCrossing = false;
  IsCrossing(Direction d1, Direction d2){
    if ((d1.end.x >= d2.start.x || d1.start.x <= d2.end.x) &&
      (d1.end.y >= d2.start.y || d1.start.y <= d2.end.y)){
        print("found match");
        hasCrossing = true;
    }
  }
}

class Direction {
  Coordinate start;
  Coordinate end;
  String mapDirection;
}

class Coordinate {
  int x;
  int y;
}