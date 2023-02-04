print(
    max(
        list(
            map(
                int, map("".join, map(reversed, input().split()))
            )
        )
    )
)
