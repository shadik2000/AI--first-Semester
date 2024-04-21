public class FormulaConverter {

    public static void main(String[] args) {
        String input = "(!d & c & !e & a)  <-> l1|\n" +
                "(c & !b & !a & !d)  <-> l2|\n" +
                "(!d & b & c & !e)  <-> l3|\n" +
                "(a & d & !c & b)  <-> l4|\n" +
                "(!b & a & d & c)  <-> l5|\n" +
                "(!d & b & !c & !e)  <-> l6|\n" +
                "(b & !e & !c & !d)  <-> l7|\n" +
                "(d & b & !a & e)  <-> l8|\n" +
                "(d & c & !b & !a)  <-> l9|\n" +
                "(!d & !a & c & b)  <-> l10|\n" +
                "(!c & !d & e & !b)  <-> l11|\n" +
                "(a & !d & !e & !c)  <-> l12|\n" +
                "(d & b & c & a)  <-> l13|\n" +
                "(e & !b & !c & d)  <-> l14|\n" +
                "(!b & !c & d & e)  <-> l15|\n" +
                "(!d & !b & !e & c)  <-> l16|\n" +
                "(b & c & d & !a)  <-> l17|\n" +
                "(!c & d & !a & !e)  <-> l18|\n" +
                "(!e & c & b & a) <-> l19";
                
                
                               
        String[] lines = input.split("\n");

        for (String line : lines) {
            String[] parts = line.split(" <-> ");
            String formula = parts[0].trim();
            String variable = parts[1].trim();

            String convertedFormula = convertFormula(formula, variable);

            System.out.println(convertedFormula);
        }
    }

    private static String convertFormula(String formula, String variable) {
        String[] literals = formula.split(" ");
        StringBuilder output = new StringBuilder();

        literals[0] = literals[0].replace("(", "");
        literals[6] = literals[6].replace((")"), "");


        for (String literal : literals) { // first part
            if (literal.equals("|") || literal.equals("&")) {
                output.append("&");
            } else {
                output.append("(!").append(variable).append(" | ").append(literal).append(")");
            }
            output.append(" ");
        }

        // second part
        output.append("(");
        for (String literal : literals) {
            if (literal.equals("|") || literal.equals("&")) {

            } else {
                if (literal.contains("!")) {
                    output.append(literal.replace("!", ""));
                } else {
                    output.append("!").append(literal);
                }
                output.append(" |");
            }
        }

        output.append(" ").append(variable).append(") &");


        return output.toString().trim();
    }
}


