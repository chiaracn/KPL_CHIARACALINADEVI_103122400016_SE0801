export async function getOrderDetails(orderId, token) {
    const response = await fetch(
        `https://example.com/api/order/${orderId}`,
        {
            headers: {
                Authorization: token
            }
        }
    );

    if (!response.ok) {
        throw new Error("Failed to fetch order details");
    }

    return response.json();
}