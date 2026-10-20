from main import (
    calculate_local_fallback,
    calculate_loyalty_locally,
)

# Existing fallback tests


def test_silver_tier():
    result = calculate_local_fallback(1000, "Silver", 100.00)

    assert result["tier_discount"] == 0.00
    assert result["final_total"] == 100.00


def test_gold_tier():
    result = calculate_local_fallback(1000, "Gold", 200.00)

    assert result["tier_discount"] == 20.00
    assert result["final_total"] == 180.00


def test_platinum_tier():
    result = calculate_local_fallback(1000, "Platinum", 200.00)

    assert result["tier_discount"] == 30.00
    assert result["final_total"] == 170.00


def test_unknown_tier():
    result = calculate_local_fallback(500, "Unknown", 100.00)

    assert result["tier_discount"] == 0.00
    assert result["final_total"] == 100.00


def test_negative_order_total():
    result = calculate_local_fallback(500, "Gold", -50.00)

    assert result["final_total"] == 0.00


def test_negative_points():
    result = calculate_local_fallback(-100, "Silver", 100.00)

    assert result["remaining_points"] == 0


def test_fallback_flag():
    result = calculate_local_fallback(1000, "Gold", 100.00)

    assert result["fallback"] is True


# Actual loyalty calculation tests


def test_points_redemption():
    result = calculate_loyalty_locally(
        loyalty_points=1000,
        tier="Silver",
        order_total=100.00,
    )

    assert result["points_redeemed"] == 1000
    assert result["points_discount"] == 10.00
    assert result["final_total"] == 90.00


def test_points_redemption_500_increment():
    result = calculate_loyalty_locally(
        loyalty_points=1250,
        tier="Silver",
        order_total=100.00,
    )

    # 1250 points rounds down to 1000
    assert result["points_redeemed"] == 1000
    assert result["remaining_points"] == 250


def test_points_redemption_cap():
    result = calculate_loyalty_locally(
        loyalty_points=10000,
        tier="Silver",
        order_total=100.00,
    )

    # Maximum redemption is 50% of the order: 5000 points
    assert result["points_redeemed"] == 5000
    assert result["points_discount"] == 50.00
    assert result["final_total"] == 50.00


def test_gold_tier_with_points():
    result = calculate_loyalty_locally(
        loyalty_points=1000,
        tier="Gold",
        order_total=100.00,
    )

    # 100 - 10 points discount = 90
    # Gold discount = 10% of 90 = 9
    assert result["tier_discount"] == 9.00
    assert result["final_total"] == 81.00


def test_platinum_tier_with_points():
    result = calculate_loyalty_locally(
        loyalty_points=1000,
        tier="Platinum",
        order_total=100.00,
    )

    assert result["tier_discount"] == 13.50
    assert result["final_total"] == 76.50


def test_standard_product_points_earned():
    result = calculate_loyalty_locally(
        loyalty_points=0,
        tier="Silver",
        order_total=100.00,
        product_category="standard",
    )

    assert result["points_earned"] == 100


def test_device_product_points_earned():
    result = calculate_loyalty_locally(
        loyalty_points=0,
        tier="Silver",
        order_total=100.00,
        product_category="device",
    )

    assert result["points_earned"] == 200


def test_fresh_product_points_earned():
    result = calculate_loyalty_locally(
        loyalty_points=0,
        tier="Silver",
        order_total=100.00,
        product_category="fresh",
    )

    assert result["points_earned"] == 500


def test_negative_points_locally():
    result = calculate_loyalty_locally(
        loyalty_points=-100,
        tier="Silver",
        order_total=100.00,
    )

    assert result["points_redeemed"] == 0
    assert result["remaining_points"] == 0
    assert result["final_total"] == 100.00


def test_unknown_product_category():
    result = calculate_loyalty_locally(
        loyalty_points=0,
        tier="Silver",
        order_total=100.00,
        product_category="unknown",
    )

    # Unknown categories use the standard rate of 1
    assert result["points_earned"] == 100
