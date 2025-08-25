from typing import List,Dict,Any,Optional
from pydantic import BaseModel, Field

class StoryOptionLLM(BaseModel):
    text: str = Field(description="the text of the option")
    nextNode: Dict[str, Any] = Field(description="the next node content and its options")


class StoryNodeLLM(BaseModel):
    content: str = Field(description="the content of the node")
    isEnding: bool = Field(description="wether this node is the end node")
    isWinningEnding: bool = Field(description="wether this node is the win end node")
    options: Optional[List[StoryOptionLLM]] = Field(default=None, description="options for this node")

class StoryLLMResponse(BaseModel):
    title: str = Field(description="The title of the story")
    rootNode: StoryNodeLLM= Field(description="thr root node of the story")