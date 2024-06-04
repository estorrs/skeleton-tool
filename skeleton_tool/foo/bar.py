from typing import Dict, Union, Optional, Any, Tuple

from typing_extensions import Annotated, Doc

class Bar():
    def __init__(
        self,
        name: Annotated[
            str,
            Doc(
                """
                This is a docstring formatted like google

                Bar wee woo

                Read more at this random [link](https://weather.gov)

                Some **bold** text

                This is a list:

                * item 1
                * item 2
                
                This is an example

                **Example**

                ```python
                from skeleton_tool.foo import bar

                bar = Bar('foo', wee=10)
                ```
                
                this is a line break

                ---

                FIN
                
                """
            )
        ],
        wee: Annotated[
            Optional[Tuple[Dict[str, Union[str, Any]]]],
            Doc(
                """
                Tuple of dictionaries for something

                Is optional
                """
            )
        ] = ({'hello': 'world!'},)
        ):
        self.name = name
        self.wee = wee
    def some_method(
        self,
        arg1: Annotated[
            str,
            Doc(
                """
                This is some arg

                It's name is arg1
                """
            )
        ]
        ) -> str:
        """
        This is the function some_method

        It does things

        **Example**
        ```python
        from skeleton_tool.foo import bar

        bar = Bar('foo', wee=10)

        value = bar.some_method('world')
        ```
        """
        return self.name + arg1