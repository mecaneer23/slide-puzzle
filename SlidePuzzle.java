import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class SlidePuzzle {
    public static void main(String[] args) {
        final int BOARD_SIZE = 3;
        ArrayList<String> board = new ArrayList<String>();
        board.add("  ");
        for (int i = 1; i < BOARD_SIZE*BOARD_SIZE; i++) {
            board.add(String.format("%2s", Integer.toString(i)));
        }
        ArrayList<String> sorted = new ArrayList<String>(board);
        Collections.shuffle(board);
        int moves = 0;
        Scanner key = new Scanner(System.in);
        while (true) {
            System.out.println("Moves: " + moves);
            moves++;
            System.out.println("    ");
            int counter = 1;
            for (String piece : board) {
                System.out.print(piece + " ");
                if (counter % BOARD_SIZE == 0) {
                    System.out.println("    ");
                }
                counter++;
            }
            System.out.print("\nMove: ");
            String inp = key.nextLine();
            if (inp == "q") {
                key.close();
                break;
            }
            String move = String.format("%2s", inp);
            int open_space_loc = board.indexOf("  ");
            int move_loc = 0;
            try {
                move_loc = board.indexOf(move);
            } catch (Exception e) {
                continue;
            }
            if (
                move_loc + 1 == open_space_loc
                || move_loc - 1 == open_space_loc
                || move_loc + BOARD_SIZE == open_space_loc
                || move_loc - BOARD_SIZE == open_space_loc
            ){
                Collections.swap(board, open_space_loc, move_loc);
            }
            if (board == sorted) {
                key.close();
                System.out.println("You win!");
                break;
            }
            for (int i = 0; i < 20; i++) System.out.print("-");
            System.out.println();
        }
    }
}