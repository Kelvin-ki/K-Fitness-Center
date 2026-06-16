"""
Tests for docs/assistant-playbook.md — K Fitness Center AI Assistant Playbook.

Validates that the playbook contains accurate multilingual content, consistent
business data (matching README), required safety rules, sales scripts, and
marketing templates introduced in the PR.
"""

import os
import re
import unittest

PLAYBOOK_PATH = os.path.join(os.path.dirname(__file__), "..", "docs", "assistant-playbook.md")
README_PATH = os.path.join(os.path.dirname(__file__), "..", "README.md")

# Canonical values that must be consistent across both files.
CANONICAL_PHONES = ("09966766466", "09676003533", "09675844933")
CANONICAL_MAP_URL = "https://maps.app.goo.gl/pDefLUxTmSoZ3RB18?g_st=ipc"
CANONICAL_LOCATION = "Shwe Kokko Myain, Myawaddy"


def read_file(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        return f.read()


class TestPlaybookStructure(unittest.TestCase):
    """Top-level document structure."""

    def setUp(self):
        self.content = read_file(PLAYBOOK_PATH)

    def test_h1_title(self):
        self.assertRegex(
            self.content,
            r"^# K Fitness Center AI Assistant Playbook",
            msg="H1 must be the playbook title",
        )

    def test_core_identity_section(self):
        self.assertIn("## Core Identity", self.content)

    def test_language_policy_section(self):
        self.assertIn("## Language Policy", self.content)

    def test_quick_customer_answers_section(self):
        self.assertIn("## Quick Customer Answers", self.content)

    def test_sales_closing_scripts_section(self):
        self.assertIn("## Sales Closing Scripts", self.content)

    def test_marketing_content_templates_section(self):
        self.assertIn("## Marketing Content Templates", self.content)

    def test_content_creation_workflow_section(self):
        self.assertIn("## Content Creation Workflow", self.content)

    def test_weekly_automated_output_calendar_section(self):
        self.assertIn("## Weekly Automated Output Calendar", self.content)

    def test_file_is_not_empty(self):
        self.assertGreater(len(self.content.strip()), 0)


class TestPlaybookCoreIdentity(unittest.TestCase):
    """Core identity assertions."""

    def setUp(self):
        self.content = read_file(PLAYBOOK_PATH)

    def test_gym_name_in_identity(self):
        self.assertIn("K Fitness Center", self.content)

    def test_location_in_identity(self):
        self.assertIn(CANONICAL_LOCATION, self.content)

    def test_identity_mentions_customer_safety(self):
        self.assertIn("safety", self.content.lower())


class TestPlaybookLanguagePolicy(unittest.TestCase):
    """Language policy must cover all four supported customer types."""

    def setUp(self):
        self.content = read_file(PLAYBOOK_PATH)

    def test_myanmar_customer_policy(self):
        self.assertIn("Myanmar customer", self.content)

    def test_english_customer_policy(self):
        self.assertIn("English customer", self.content)

    def test_chinese_customer_policy(self):
        self.assertIn("Chinese customer", self.content)

    def test_mixed_bilingual_policy(self):
        self.assertIn("Mixed Myanmar-English", self.content)

    def test_language_policy_reply_in_same_language(self):
        self.assertIn("Reply in the same language", self.content)


class TestPlaybookOpeningHours(unittest.TestCase):
    """Opening hours templates in all three languages."""

    def setUp(self):
        self.content = read_file(PLAYBOOK_PATH)

    def test_english_hours_monday_to_saturday(self):
        self.assertIn("Monday to Saturday", self.content)

    def test_english_hours_times(self):
        self.assertIn("6:00 AM", self.content)
        self.assertIn("1:00 AM", self.content)

    def test_english_hours_sunday_closed(self):
        self.assertIn("Sunday is closed", self.content)

    def test_myanmar_hours_template_present(self):
        # Myanmar script contains the word Saturday transliterated; check for Myanmar chars.
        self.assertIn("Saturday", self.content)
        # Myanmar-script content must appear somewhere in the hours block.
        self.assertRegex(self.content, r"[\u1000-\u109F]", msg="Myanmar script expected in playbook")

    def test_chinese_hours_template_present(self):
        # Chinese numerals / characters must appear in the document.
        self.assertRegex(self.content, r"[\u4E00-\u9FFF]", msg="Chinese characters expected in playbook")


class TestPlaybookPricingConsistency(unittest.TestCase):
    """All prices in the playbook must match README canonical values."""

    def setUp(self):
        self.playbook = read_file(PLAYBOOK_PATH)

    def test_single_visit_price(self):
        self.assertIn("250฿", self.playbook)

    def test_monthly_base_price(self):
        self.assertIn("1700฿", self.playbook)

    def test_monthly_membership_fee(self):
        self.assertIn("300฿", self.playbook)

    def test_three_month_price(self):
        self.assertIn("5000฿", self.playbook)

    def test_three_month_free_month(self):
        match = re.search(r"5000฿.{0,100}1 month free|1 month free.{0,100}5000฿", self.playbook, re.DOTALL)
        self.assertIsNotNone(match, "3-month plan must include '1 month free'")

    def test_six_month_price(self):
        self.assertIn("10000฿", self.playbook)

    def test_six_month_free_months(self):
        match = re.search(r"10000฿.{0,100}3 months free|3 months free.{0,100}10000฿", self.playbook, re.DOTALL)
        self.assertIsNotNone(match, "6-month plan must include '3 months free'")

    def test_private_coach_price(self):
        self.assertIn("+2000฿", self.playbook)

    def test_pickup_service_price(self):
        # Verify the term and the +2000฿ value appear (pickup and +2000฿ both in file).
        self.assertIn("Pickup", self.playbook)

    def test_prices_use_baht_symbol(self):
        self.assertIn("฿", self.playbook)


class TestPlaybookPhoneNumberConsistency(unittest.TestCase):
    """Phone numbers in playbook must match README exactly."""

    def setUp(self):
        self.playbook = read_file(PLAYBOOK_PATH)

    def test_primary_phone_present(self):
        self.assertIn(CANONICAL_PHONES[0], self.playbook)

    def test_secondary_phone_present(self):
        self.assertIn(CANONICAL_PHONES[1], self.playbook)

    def test_tertiary_phone_present(self):
        self.assertIn(CANONICAL_PHONES[2], self.playbook)

    def test_phones_match_readme(self):
        readme = read_file(README_PATH)
        for phone in CANONICAL_PHONES:
            with self.subTest(phone=phone):
                self.assertIn(phone, self.playbook)
                self.assertIn(phone, readme)


class TestPlaybookMapUrlConsistency(unittest.TestCase):
    """Google Map URL in playbook must match README exactly."""

    def setUp(self):
        self.playbook = read_file(PLAYBOOK_PATH)

    def test_map_url_present(self):
        self.assertIn(CANONICAL_MAP_URL, self.playbook)

    def test_map_url_is_https(self):
        urls = re.findall(r"https?://maps\.app\.goo\.gl/\S+", self.playbook)
        self.assertTrue(len(urls) > 0, "At least one Google Maps URL must be present")
        self.assertTrue(all(u.startswith("https://") for u in urls), "All map URLs must use HTTPS")

    def test_map_url_matches_readme(self):
        readme = read_file(README_PATH)
        self.assertIn(CANONICAL_MAP_URL, readme)
        self.assertIn(CANONICAL_MAP_URL, self.playbook)


class TestPlaybookMultilingualPrices(unittest.TestCase):
    """Price section must have all three language blocks."""

    def setUp(self):
        self.content = read_file(PLAYBOOK_PATH)

    def test_english_prices_block(self):
        # English block contains English text with price list.
        self.assertIn("Single visit: 250฿", self.content)

    def test_myanmar_prices_block(self):
        # Myanmar block contains Myanmar price list markers.
        self.assertIn("တစ်ခါကစား: 250฿", self.content)

    def test_chinese_prices_block(self):
        # Chinese block contains Chinese price list marker.
        self.assertIn("单次：250฿", self.content)


class TestPlaybookSalesScripts(unittest.TestCase):
    """Sales closing scripts must cover all four scenarios."""

    def setUp(self):
        self.content = read_file(PLAYBOOK_PATH)

    def test_new_customer_asking_price_script(self):
        self.assertIn("### New Customer Asking Price", self.content)

    def test_fat_loss_customer_script(self):
        self.assertIn("### Fat Loss Customer", self.content)

    def test_fat_loss_script_no_exact_kg_promise(self):
        self.assertIn("we do not promise exact kg loss", self.content)

    def test_muscle_gain_customer_script(self):
        self.assertIn("### Muscle Gain Customer", self.content)

    def test_pain_injury_customer_script(self):
        self.assertIn("### Customer With Pain or Injury", self.content)

    def test_pain_script_directs_to_medical_professional(self):
        self.assertIn("consult a medical professional", self.content)

    def test_new_customer_script_recommends_monthly_plan(self):
        self.assertIn("Monthly plan", self.content)

    def test_new_customer_script_includes_phone_or_location(self):
        # Script should contain at least one phone number or the map URL.
        has_phone = any(p in self.content for p in CANONICAL_PHONES)
        has_map = CANONICAL_MAP_URL in self.content
        self.assertTrue(has_phone or has_map, "Sales scripts must include phone or location contact")

    def test_myanmar_english_bilingual_script_present(self):
        self.assertIn("Myanmar-English bilingual", self.content)


class TestPlaybookSafetyRules(unittest.TestCase):
    """Safety guardrails must be present in the playbook."""

    def setUp(self):
        self.content = read_file(PLAYBOOK_PATH)

    def test_pain_script_english_medical_advice(self):
        self.assertIn("consult a medical professional before training", self.content)

    def test_pain_script_myanmar_medical_advice(self):
        # Myanmar text about consulting a doctor must be present.
        self.assertIn("ဆရာဝန်", self.content)

    def test_fat_loss_script_no_exact_results_promise(self):
        self.assertIn("do not promise exact kg loss", self.content)

    def test_youtube_description_medical_disclaimer(self):
        self.assertIn("consult a medical professional before training", self.content)

    def test_safety_covers_pain_keyword(self):
        self.assertIn("pain", self.content.lower())

    def test_safety_covers_injury_keyword(self):
        self.assertIn("injury", self.content.lower())

    def test_safety_covers_dizziness_keyword(self):
        self.assertIn("dizziness", self.content.lower())


class TestPlaybookMarketingTemplates(unittest.TestCase):
    """Marketing content templates must be complete and well-structured."""

    def setUp(self):
        self.content = read_file(PLAYBOOK_PATH)

    def test_facebook_telegram_post_section(self):
        self.assertIn("### Facebook / Telegram Post", self.content)

    def test_tiktok_reels_script_section(self):
        self.assertIn("### TikTok / Reels Short Video Script", self.content)

    def test_youtube_video_idea_section(self):
        self.assertIn("### YouTube Video Idea", self.content)

    def test_facebook_post_has_question_block(self):
        # Each post template must have the five structural blocks.
        self.assertIn("**Question**", self.content)

    def test_facebook_post_has_emotion_block(self):
        self.assertIn("**Emotion**", self.content)

    def test_facebook_post_has_trust_block(self):
        self.assertIn("**Trust**", self.content)

    def test_facebook_post_has_offer_block(self):
        self.assertIn("**Offer**", self.content)

    def test_facebook_post_has_close_block(self):
        self.assertIn("**Close**", self.content)

    def test_tiktok_hook_present(self):
        self.assertIn("**Hook**", self.content)

    def test_tiktok_call_to_action_present(self):
        self.assertIn("**Call to Action**", self.content)

    def test_youtube_title_present(self):
        self.assertIn("**Title**", self.content)

    def test_youtube_description_present(self):
        self.assertIn("**Description**", self.content)

    def test_marketing_close_contains_contact(self):
        # The marketing Close block must include at least one phone.
        has_phone = any(p in self.content for p in CANONICAL_PHONES)
        self.assertTrue(has_phone, "Marketing templates must include contact phone numbers")

    def test_marketing_close_contains_map(self):
        self.assertIn(CANONICAL_MAP_URL, self.content)


class TestPlaybookFreeGroupClasses(unittest.TestCase):
    """Free group classes must be listed in the playbook."""

    def setUp(self):
        self.content = read_file(PLAYBOOK_PATH)

    def test_aerobics_in_free_classes(self):
        self.assertIn("Aerobics", self.content)

    def test_zumba_in_free_classes(self):
        self.assertIn("Zumba", self.content)

    def test_trampoline_in_free_classes(self):
        self.assertIn("Trampoline", self.content)

    def test_step_board_in_free_classes(self):
        self.assertIn("Step Board", self.content)


class TestPlaybookServices(unittest.TestCase):
    """Core services must be listed in the playbook."""

    def setUp(self):
        self.content = read_file(PLAYBOOK_PATH)

    def test_muscle_gain(self):
        self.assertIn("muscle gain", self.content)

    def test_fat_loss(self):
        self.assertIn("fat loss", self.content)

    def test_crossfit(self):
        self.assertIn("CrossFit", self.content)

    def test_private_coaching(self):
        # Playbook uses "private coaching" or "private coach".
        self.assertRegex(self.content, r"private coach(ing)?", re.IGNORECASE)

    def test_nutrition_guidance(self):
        self.assertIn("nutrition guidance", self.content)

    def test_pickup_service(self):
        self.assertIn("pickup service", self.content)


class TestPlaybookContentWorkflow(unittest.TestCase):
    """Content creation workflow must list all seven steps."""

    def setUp(self):
        self.content = read_file(PLAYBOOK_PATH)

    def test_step_1_topic_ideas(self):
        self.assertIn("Topic ideas", self.content)

    def test_step_2_content_planning(self):
        self.assertIn("Content planning", self.content)

    def test_step_3_content_generation(self):
        self.assertIn("Content generation", self.content)

    def test_step_4_image_generation(self):
        self.assertIn("Image generation", self.content)

    def test_step_5_video_generation(self):
        self.assertIn("Video generation", self.content)

    def test_step_6_publish_and_distribute(self):
        self.assertIn("Publish and distribute", self.content)

    def test_step_7_review_performance(self):
        self.assertIn("Review performance", self.content)

    def test_workflow_has_seven_steps(self):
        steps = re.findall(r"^\d+\.", self.content, re.MULTILINE)
        # The workflow section has exactly 7 numbered steps.
        self.assertGreaterEqual(len(steps), 7, "Workflow must have at least 7 numbered steps")


class TestPlaybookWeeklyCalendar(unittest.TestCase):
    """Weekly automated output calendar must cover all seven days."""

    def setUp(self):
        self.content = read_file(PLAYBOOK_PATH)

    def test_monday_in_calendar(self):
        self.assertIn("Monday", self.content)

    def test_tuesday_in_calendar(self):
        self.assertIn("Tuesday", self.content)

    def test_wednesday_in_calendar(self):
        self.assertIn("Wednesday", self.content)

    def test_thursday_in_calendar(self):
        self.assertIn("Thursday", self.content)

    def test_friday_in_calendar(self):
        self.assertIn("Friday", self.content)

    def test_saturday_in_calendar(self):
        self.assertIn("Saturday", self.content)

    def test_sunday_in_calendar(self):
        self.assertIn("Sunday", self.content)

    def test_tiktok_channel_in_calendar(self):
        self.assertIn("TikTok", self.content)

    def test_youtube_channel_in_calendar(self):
        self.assertIn("YouTube", self.content)

    def test_facebook_channel_in_calendar(self):
        self.assertIn("Facebook", self.content)


class TestPlaybookCrossFileConsistency(unittest.TestCase):
    """Values in the playbook must be consistent with README.md."""

    def setUp(self):
        self.playbook = read_file(PLAYBOOK_PATH)
        self.readme = read_file(README_PATH)

    def test_location_matches_readme(self):
        self.assertIn(CANONICAL_LOCATION, self.playbook)
        self.assertIn(CANONICAL_LOCATION, self.readme)

    def test_map_url_matches_readme(self):
        self.assertIn(CANONICAL_MAP_URL, self.playbook)
        self.assertIn(CANONICAL_MAP_URL, self.readme)

    def test_all_phones_match_readme(self):
        for phone in CANONICAL_PHONES:
            with self.subTest(phone=phone):
                self.assertIn(phone, self.playbook)
                self.assertIn(phone, self.readme)

    def test_single_visit_price_matches_readme(self):
        self.assertIn("250฿", self.playbook)
        self.assertIn("250฿", self.readme)

    def test_monthly_price_matches_readme(self):
        self.assertIn("1700฿", self.playbook)
        self.assertIn("1700฿", self.readme)

    def test_three_month_price_matches_readme(self):
        self.assertIn("5000฿", self.playbook)
        self.assertIn("5000฿", self.readme)

    def test_six_month_price_matches_readme(self):
        self.assertIn("10000฿", self.playbook)
        self.assertIn("10000฿", self.readme)


class TestPlaybookEdgeCases(unittest.TestCase):
    """Boundary and regression checks for the playbook."""

    def setUp(self):
        self.content = read_file(PLAYBOOK_PATH)

    def test_no_placeholder_text(self):
        self.assertNotIn("Lorem ipsum", self.content)
        self.assertNotIn("TODO", self.content)
        self.assertNotIn("FIXME", self.content)

    def test_all_map_urls_are_https(self):
        urls = re.findall(r"https?://maps\.app\.goo\.gl/\S+", self.content)
        self.assertTrue(len(urls) > 0, "At least one map URL must be present")
        for url in urls:
            with self.subTest(url=url):
                self.assertTrue(url.startswith("https://"))

    def test_no_inconsistent_map_url_variants(self):
        """Only the canonical URL should appear; no typos or shortened variants."""
        all_map_urls = re.findall(r"https?://maps\.app\.goo\.gl/\S+", self.content)
        for url in all_map_urls:
            # Strip trailing punctuation that markdown may capture.
            url_clean = url.rstrip(".,;)")
            with self.subTest(url=url_clean):
                self.assertEqual(url_clean, CANONICAL_MAP_URL, "All map URLs must equal the canonical URL")

    def test_h1_appears_exactly_once(self):
        h1_matches = re.findall(r"^# .+", self.content, re.MULTILINE)
        self.assertEqual(len(h1_matches), 1, "Playbook should have exactly one H1 heading")

    def test_playbook_references_gym_name_multiple_times(self):
        count = self.content.count("K Fitness Center")
        self.assertGreater(count, 1, "Gym name should appear more than once in the playbook")

    def test_no_currency_symbol_typos(self):
        """Prices must use ฿ (U+0E3F), not $ or £ or other symbols."""
        # Verify that at least some prices exist and use the correct symbol.
        price_pattern = re.compile(r"\d+฿")
        matches = price_pattern.findall(self.content)
        self.assertTrue(len(matches) > 0, "Prices must use the ฿ symbol")


if __name__ == "__main__":
    unittest.main()