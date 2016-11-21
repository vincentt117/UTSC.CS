package ui;

import game.Constants;
import game.VacuumGame;
import sprites.Vacuum;

import java.util.Scanner;

import javax.swing.JOptionPane;

/**
 * A text UI for the game.
 * 
 * @author tengvinc
 *
 */
public class TextUi implements Ui {
  private VacuumGame game;

  /**
   * Initializes a TextUI for the given VacuumGame.
   * 
   * @param game
   *          The VacuumGame of this GUI
   */
  public TextUi(VacuumGame game) {
    this.game = game;
  }

  @Override
  public void launchGame() {
    // TODO Auto-generated method stub
    System.out.println(game.displayGame());
    Scanner sc = new Scanner(System.in);
    // Await user input
    char nextMove;
    while (sc.hasNextLine() && !game.gameOver()) {
      nextMove = sc.next().charAt(0);
      game.move(nextMove);
      System.out.println(game.displayGame());
    }
    sc.close();
  }

  @Override
  public void displayWinner() {
    // TODO Auto-generated method stub
    if (!game.gameOver()) {
      return;
    }
    char won = game.getWinner();
    String message;
    if (won == Constants.TIE) {
      message = "It's a tie!";
    } else {
      Vacuum winner = (won == Constants.P1) ? game.getVacuumOne() : game.getVacuumTwo();
      int score = winner.getScore();
      message = String.format("Congratulations Player %s! You won the game with a score of %d.",
          winner.toString(), score);
    }
    JOptionPane.showMessageDialog(null, message);
  }

}
