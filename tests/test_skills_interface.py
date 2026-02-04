import pytest


def test_skills_interface_contracts():
    # These tests define the "empty slots" for runtime skills.
    # They should fail until the skills are implemented.
    from skills.skill_download_youtube import skill_download_youtube
    from skills.skill_transcribe_audio import skill_transcribe_audio
    from skills.skill_trend_analyzer import skill_trend_analyzer

    # Interface: accepts required parameters
    with pytest.raises(NotImplementedError):
        skill_download_youtube(youtube_url="https://example.com/watch?v=dQw4w9WgXcQ")

    with pytest.raises(NotImplementedError):
        skill_transcribe_audio(local_file_path="./media/sample.mp4")

    with pytest.raises(NotImplementedError):
        skill_trend_analyzer(news_resource="mcp://news/trends")
