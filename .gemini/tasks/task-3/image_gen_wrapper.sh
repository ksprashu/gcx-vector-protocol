#!/bin/bash
# Load GEMINI_API_KEY and map it to GOOGLE_API_KEY for the script
if [ -f /Users/ksprashanth/.gemini/.env ]; then
    export GOOGLE_API_KEY=$(grep "^GEMINI_API_KEY=" /Users/ksprashanth/.gemini/.env | cut -d'=' -f2)
fi

if [ -z "$GOOGLE_API_KEY" ]; then
    echo "❌ Error: GOOGLE_API_KEY not found."
    exit 1
fi

uv run --with "google-genai>=0.1.1" --with "Pillow>=10.0.0" python3 /Users/ksprashanth/.gemini/skills/image-gen-expert/scripts/image_gen.py \
    --prompt "A clean, flat vector infographic illustrating the 'Zero-Context Orchestration' concept. The image shows a central hub representing a shared fractal filesystem (labeled '.gemini/'). Multiple isolated robotic agents are positioned around the hub, each working within its own distinct section of the filesystem (labeled 'task-1', 'task-2', etc.). Lines or data streams connect the agents to their respective fractal directories. The style is professional, using a technical color palette (blue, slate, and white) with clear labels. The title on the image reads 'Zero-Context Orchestration'." \
    --ar "1:1" \
    --output "/Users/ksprashanth/code/github/gcx-vector-protocol/.gemini/assets/zero_context_infographic.png"
