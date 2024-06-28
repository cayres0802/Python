#include <stdio.h>

int main() {
    double numRides, avgDistance, avgPrice, gasCost, totalMiles, totalGasCost, totalProfit;
    double distance;

    printf("Enter the number of rides: ");
    scanf("%lf", &numRides);

    totalMiles = 0;
    for (int i = 0; i < numRides; i++) {
        printf("Enter the distance of ride %d: ", i+1);
        scanf("%lf", &distance);
        totalMiles += distance;
    }

    printf("Enter the average distance per ride: ");
    scanf("%lf", &avgDistance);

    totalMiles = numRides * avgDistance;

    printf("Enter the average price per ride: ");
    scanf("%lf", &avgPrice);

    printf("Enter the cost of gas per gallon: ");
    scanf("%lf", &gasCost);

    totalGasCost = totalMiles * gasCost;

    // Calculate total profit here

    return 0;
}