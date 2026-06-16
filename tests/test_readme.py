"""
Tests for README.md — K Fitness Center knowledge base.

Validates that the README contains accurate, complete business information,
safety rules, AI assistant directives, and marketing structure as defined
in the PR that introduced the content.
"""

import os
import re
import unittest

README_PATH = os.path.join(os.path.dirname(__file__), "..", "README.md")


def read_readme() -> str:
    with open(README_PATH, encoding="utf-8") as f:
        return f.read()


class TestReadmeStructure(unittest.TestCase):
    """Top-level structure and required sections."""

    def setUp(self):
        self.content = read_readme()

    def test_h1_title_is_k_fitness_center(self):
        """README must open with the exact gym name as H1."""
        self.assertRegex(self.content, r"^# K Fitness Center\b", msg="H1 heading must be 'K Fitness Center'")

    def test_business_source_of_truth_section_exists(self):
        """'Business Source of Truth' section must be present."""
        self.assertIn("## Business Source of Truth", self.content)

    def test_ai_assistant_role_section_exists(self):
        """'Official AI Assistant Role' section must be present."""
        self.assertIn("## Official AI Assistant Role", self.content)

    def test_sales_style_section_exists(self):
        """'Sales Style' section must be present."""
        self.assertIn("## Sales Style", self.content)

    def test_safety_rules_section_exists(self):
        """'Safety Rules' section must be present."""
        self.assertIn("## Safety Rules", self.content)

    def test_marketing_post_structure_section_exists(self):
        """'Marketing Post Structure' section must be present."""
        self.assertIn("## Marketing Post Structure", self.content)

    def test_playbook_link_present(self):
        """README must link to docs/assistant-playbook.md."""
        self.assertIn("docs/assistant-playbook.md", self.content)


class TestReadmeBusinessInfo(unittest.TestCase):
    """Core business facts that must appear verbatim in the README."""

    def setUp(self):
        self.content = read_readme()

    def test_gym_name_in_business_table(self):
        self.assertIn("K Fitness Center", self.content)

    def test_location_shwe_kokko_myain(self):
        self.assertIn("Shwe Kokko Myain", self.content)

    def test_location_myawaddy(self):
        self.assertIn("Myawaddy", self.content)

    def test_google_map_url_present(self):
        self.assertIn(
            "https://maps.app.goo.gl/pDefLUxTmSoZ3RB18?g_st=ipc",
            self.content,
        )

    def test_all_three_phone_numbers_present(self):
        for phone in ("09966766466", "09676003533", "09675844933"):
            with self.subTest(phone=phone):
                self.assertIn(phone, self.content)

    def test_opening_hours_monday_to_saturday(self):
        self.assertIn("Monday to Saturday", self.content)

    def test_opening_hours_start_time(self):
        self.assertIn("6:00 AM", self.content)

    def test_opening_hours_end_time(self):
        self.assertIn("1:00 AM", self.content)

    def test_sunday_closed(self):
        self.assertIn("Sunday", self.content)
        self.assertIn("Closed", self.content)


class TestReadmePricing(unittest.TestCase):
    """Membership and service pricing must match the canonical business data."""

    def setUp(self):
        self.content = read_readme()

    def test_single_visit_price(self):
        self.assertIn("250฿", self.content)

    def test_monthly_plan_base_price(self):
        self.assertIn("1700฿", self.content)

    def test_monthly_plan_membership_fee(self):
        self.assertIn("300฿", self.content)

    def test_three_month_plan_price(self):
        self.assertIn("5000฿", self.content)

    def test_three_month_plan_free_month(self):
        # Must mention 1 free month alongside the 3-month plan.
        match = re.search(r"5000฿.*1 month free|1 month free.*5000฿", self.content, re.DOTALL)
        self.assertIsNotNone(match, "3-month plan must mention '1 month free'")

    def test_six_month_plan_price(self):
        self.assertIn("10000฿", self.content)

    def test_six_month_plan_free_months(self):
        match = re.search(r"10000฿.*3 months free|3 months free.*10000฿", self.content, re.DOTALL)
        self.assertIsNotNone(match, "6-month plan must mention '3 months free'")

    def test_private_coach_additional_cost(self):
        self.assertIn("+2000฿", self.content)

    def test_pickup_service_additional_cost(self):
        # Both private coach and pickup are +2000฿; verify the table row labels exist.
        self.assertIn("Pickup", self.content)
        self.assertIn("Private Coach", self.content)


class TestReadmeFreeGroupClasses(unittest.TestCase):
    """All four free group classes must be listed."""

    def setUp(self):
        self.content = read_readme()

    def test_aerobics_in_free_classes(self):
        self.assertIn("Aerobics", self.content)

    def test_zumba_in_free_classes(self):
        self.assertIn("Zumba", self.content)

    def test_trampoline_in_free_classes(self):
        self.assertIn("Trampoline", self.content)

    def test_step_board_in_free_classes(self):
        self.assertIn("Step Board", self.content)


class TestReadmeServices(unittest.TestCase):
    """Core services must be enumerated."""

    def setUp(self):
        self.content = read_readme()

    def test_muscle_gain_service(self):
        self.assertIn("Muscle gain", self.content)

    def test_fat_loss_service(self):
        self.assertIn("fat loss", self.content)

    def test_crossfit_service(self):
        self.assertIn("CrossFit", self.content)

    def test_nutrition_guidance_service(self):
        self.assertIn("nutrition guidance", self.content)

    def test_pickup_service(self):
        self.assertIn("pickup service", self.content)


class TestReadmeAIAssistantRole(unittest.TestCase):
    """AI assistant directives must be spelled out."""

    def setUp(self):
        self.content = read_readme()

    def test_assistant_handles_prices_topic(self):
        self.assertIn("prices", self.content)

    def test_assistant_handles_opening_hours_topic(self):
        self.assertIn("opening hours", self.content)

    def test_assistant_handles_services_topic(self):
        self.assertIn("services", self.content)

    def test_assistant_generates_marketing_posts(self):
        self.assertIn("marketing posts", self.content)

    def test_assistant_supports_myanmar_language(self):
        self.assertIn("Myanmar", self.content)

    def test_assistant_supports_english_language(self):
        self.assertIn("English", self.content)

    def test_assistant_supports_chinese_language(self):
        self.assertIn("Chinese", self.content)

    def test_assistant_supports_bilingual_style(self):
        self.assertIn("bilingual", self.content)


class TestReadmeSalesStyle(unittest.TestCase):
    """Recommended sales flow must include all four steps."""

    def setUp(self):
        self.content = read_readme()

    def test_sales_flow_step_answer_question(self):
        self.assertIn("Answer the question directly", self.content)

    def test_sales_flow_step_highlight_benefit(self):
        self.assertIn("Highlight the customer benefit", self.content)

    def test_sales_flow_step_recommend_plan(self):
        self.assertIn("Recommend the best plan", self.content)

    def test_sales_flow_step_next_action(self):
        self.assertIn("Ask for the next action", self.content)

    def test_sales_include_contact_on_close(self):
        self.assertIn("contact number", self.content)


class TestReadmeSafetyRules(unittest.TestCase):
    """All four safety constraints must appear explicitly."""

    def setUp(self):
        self.content = read_readme()

    def test_no_medical_diagnosis_rule(self):
        self.assertIn("Do not provide medical diagnosis", self.content)

    def test_no_exact_weight_loss_promise_rule(self):
        self.assertIn("Do not promise exact weight-loss results", self.content)

    def test_health_condition_redirect_rule(self):
        self.assertIn("consult a qualified medical professional", self.content)

    def test_fitness_guidance_general_disclaimer(self):
        self.assertIn("not a replacement for professional medical advice", self.content)

    def test_triggers_include_pain_and_injury(self):
        self.assertIn("pain", self.content)
        self.assertIn("injury", self.content)

    def test_triggers_include_pregnancy(self):
        self.assertIn("pregnancy", self.content)


class TestReadmeMarketingPostStructure(unittest.TestCase):
    """Marketing post template must contain all five structural steps."""

    def setUp(self):
        self.content = read_readme()

    def test_marketing_step_question(self):
        self.assertIn("Question", self.content)

    def test_marketing_step_emotion(self):
        self.assertIn("Emotion", self.content)

    def test_marketing_step_trust(self):
        self.assertIn("Trust", self.content)

    def test_marketing_step_offer(self):
        self.assertIn("Offer", self.content)

    def test_marketing_step_close(self):
        self.assertIn("Close", self.content)

    def test_marketing_platforms_facebook(self):
        self.assertIn("Facebook", self.content)

    def test_marketing_platforms_telegram(self):
        self.assertIn("Telegram", self.content)

    def test_marketing_platforms_tiktok(self):
        self.assertIn("TikTok", self.content)

    def test_marketing_platforms_youtube(self):
        self.assertIn("YouTube", self.content)


class TestReadmeEdgeCases(unittest.TestCase):
    """Boundary and regression checks."""

    def setUp(self):
        self.content = read_readme()

    def test_file_is_not_empty(self):
        self.assertGreater(len(self.content.strip()), 0)

    def test_no_placeholder_text_remains(self):
        """Ensure no Lorem Ipsum or placeholder text leaked into the file."""
        self.assertNotIn("Lorem ipsum", self.content)
        self.assertNotIn("TODO", self.content)
        self.assertNotIn("FIXME", self.content)

    def test_google_map_url_is_https(self):
        urls = re.findall(r"https?://maps\.app\.goo\.gl/\S+", self.content)
        self.assertTrue(all(u.startswith("https://") for u in urls), "All map URLs must use HTTPS")

    def test_phone_numbers_are_numeric(self):
        """Phone numbers listed in the table should be numeric strings."""
        for phone in ("09966766466", "09676003533", "09675844933"):
            self.assertTrue(phone.isdigit(), f"Phone number {phone} should be all digits")

    def test_prices_use_baht_symbol(self):
        """Prices must use the Thai Baht symbol ฿, not plain numbers alone."""
        self.assertIn("฿", self.content)

    def test_h1_appears_exactly_once(self):
        h1_matches = re.findall(r"^# .+", self.content, re.MULTILINE)
        self.assertEqual(len(h1_matches), 1, "README should have exactly one H1 heading")


if __name__ == "__main__":
    unittest.main()
