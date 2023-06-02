import java.awt.*;
import java.awt.event.*;

public class MarksEntryGUI extends Frame {
    private TextField nameField;
    private TextField[] marksFields;
    
    public MarksEntryGUI() {
        setTitle("Marks Entry");
        setSize(400, 300);
        setResizable(false);
        setLayout(new FlowLayout());
        
        Label nameLabel = new Label("Student Name:");
        add(nameLabel);
        
        nameField = new TextField(20);
        add(nameField);
        
        String[] subjects = { "English", "Mathematics", "Science", "History" };
        marksFields = new TextField[subjects.length];
        
        for (int i = 0; i < subjects.length; i++) {
            Label subjectLabel = new Label(subjects[i]);
            add(subjectLabel);
            
            TextField marksField = new TextField(5);
            marksFields[i] = marksField;
            add(marksField);
        }
        
        Button submitButton = new Button("Submit");
        submitButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                submitMarks();
            }
        });
        add(submitButton);
        
        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) {
                System.exit(0);
            }
        });
    }
    
    private void submitMarks() {
        String name = nameField.getText();
        int[] marks = new int[marksFields.length];
        
        for (int i = 0; i < marksFields.length; i++) {
            marks[i] = Integer.parseInt(marksFields[i].getText());
        }
        
        if (name.isEmpty() || !areMarksValid(marks)) {
            showErrorDialog("Please enter valid name and marks for all subjects.");
        } else {
            showResultDialog(name, marks);
            clearFields();
        }
    }
    
    private boolean areMarksValid(int[] marks) {
        for (int mark : marks) {
            if (mark < 0 || mark > 100) {
                return false;
            }
        }
        return true;
    }
    
    private void showResultDialog(String name, int[] marks) {
        int totalMarks = 0;
        for (int mark : marks) {
            totalMarks += mark;
        }
        
        double percentage = (double) totalMarks / (marks.length * 100) * 100;
        String grade = calculateGrade(percentage);
        
        String resultMessage = "Result for " + name + "\n\n"
                + "Percentage: " + String.format("%.2f", percentage) + "%\n"
                + "Grade: " + grade;
        
        Dialog resultDialog = new Dialog(this, "Result", true);
        resultDialog.setSize(300, 150);
        resultDialog.setLayout(new FlowLayout());
        
        Label resultLabel = new Label(resultMessage);
        resultDialog.add(resultLabel);
        
        Button okButton = new Button("OK");
        okButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                resultDialog.dispose();
            }
        });
        resultDialog.add(okButton);
        
        resultDialog.setVisible(true);
    }
    
    private String calculateGrade(double percentage) {
        if (percentage >= 90) {
            return "A+";
        } else if (percentage >= 80) {
            return "A";
        } else if (percentage >= 70) {
            return "B";
        } else if (percentage >= 60) {
            return "C";
        } else if (percentage >= 50) {
            return "D";
        } else {
            return "F";
        }
    }
    
    private void showErrorDialog(String errorMessage) {
        Dialog errorDialog = new Dialog(this, "Error", true);
        errorDialog.setSize(250, 100);
        errorDialog.setLayout(new FlowLayout());
        
        Label errorLabel = new Label(errorMessage);
        errorDialog.add(errorLabel);
        
        Button okButton = new Button("OK");
        okButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                errorDialog.dispose();
            }
        });
        errorDialog.add(okButton);
        
        errorDialog.setVisible(true);
    }
    
    private void clearFields() {
        nameField.setText("");
        for (TextField marksField : marksFields) {
            marksField.setText("");
        }
    }
    
    public static void main(String[] args) {
        MarksEntryGUI gui = new MarksEntryGUI();
        gui.setVisible(true);
    }
}
