package Solution;
import java.lang.Math;

public class Knapsack {
    private final int[] weights = { 3, 1, 6, 10, 1, 4, 9, 1, 7, 2, 6, 1, 6, 2, 2, 4, 8, 1, 7, 3, 6, 2, 9, 5, 3, 3, 4, 7, 3, 5 };
    private final int[] costs = { 7, 4, 9, 18, 9, 15, 4, 2, 6, 13, 18, 12, 12, 16, 19, 19, 10, 16, 14, 3, 14, 4, 15, 7, 5, 10, 10, 13, 19, 9};

    public Knapsack() {
    }

    public void optimalize(){
        final long startTime = System.currentTimeMillis();
        String bestCombination = "";
        int bestCost = 0;
        int bestWeight = 0;
        double number_of_combinations = Math.pow(2, weights.length);

        for (int i = 0; i < number_of_combinations; i++) {
            StringBuilder binary = new StringBuilder(Integer.toBinaryString(i));
            for(int j = binary.length(); j < weights.length; j++) {
                binary.insert( 0, '0' );
            }

            int[] newCostWeight = maxCost(binary);

            if(newCostWeight[0] > bestCost) {
                bestCost = newCostWeight[0];
                bestWeight = newCostWeight[1];
                bestCombination = binary.toString();
            }
        }
        final long endTime = System.currentTimeMillis();

        System.out.println("Best combination: " + bestCombination);
        System.out.println("Cost: " + bestCost);
        System.out.println("Weight: " + bestWeight);
        System.out.println("Total execution time: " + (endTime - startTime));

    }

    public int[] maxCost(StringBuilder binaryStringBuilder){
        int weight = 0;
        int cost = 0;
        String binaryString = binaryStringBuilder.toString();
        for(int i = 0; i < binaryString.length(); i++){
            if(binaryString.charAt(i) == '1'){
                weight += this.weights[i];
                cost += this.costs[i];

                int wmax = 40;
                if (weight > wmax) {
                    return new int[] {0, 0};
                }
            }
        }
        return new int[] {cost, weight};
    }
}


