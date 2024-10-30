import java.util.Scanner;

class Robot
    {
        // this class makes a robot that comes with directional movement 
        double x_postion = 0.0;
        double y_postion = 0.0;
        
        public  void  moveFoward()
        {
            y_postion ++;
            System.out.println("Move forward to("+x_postion+","+y_postion+")"); 
        }
        public void moveBackward()
        {
            y_postion--;
            System.out.println("Move Back to("+x_postion+","+y_postion+")");
        }
        public void moveLeft()
        {
            x_postion--;
            System.out.println("Move Left to("+x_postion+","+y_postion+")");
        }
        public void moveRight()
        {
            x_postion++;
            System.out.println("Move Right to("+x_postion+","+y_postion+")");
        }
        public void DISPLAY()
        {
            System.out.println("Current position("+x_postion+","+y_postion+")");
        }
        
    }
// Runs the program
public class Main
    {
        public static void main(String[] args)
        {
            // creates the robot
              Robot mep = new Robot();
              System.out.println(" This is your robot: "+mep);
              Scanner scan = new Scanner(System.in);
              // using a while loop to keep on runt the program
              while(true)
              {
                // ask user for which direction the robot should move 
                System.out.println("Which direction? front, back,left,right");
                String choice = scan.nextLine();
                if (choice.equals("left"))
                {
                     mep.moveLeft();
                }
                else if(choice.equals("right"))
                {
                    mep.moveRight();
                }
                else if(choice.equals("back"))
                {
                     mep.moveBackward();
                }
                else if(choice.equals("front"))
                {
                     mep.moveFoward();
                }
                else if (choice.equals("auto"))
                {
                    
                    int auto = 5;
                    for(int i = 0; i < 5; i++)
                    {
                        mep.moveFoward();
                    }
                }
                else
                {
                  break;  
                }
              }
        }
    } 
