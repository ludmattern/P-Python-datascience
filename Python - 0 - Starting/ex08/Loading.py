def ft_tqdm(lst: range) -> None:
    """
    Custom implementation of tqdm progress bar.
    No imports allowed - pure Python implementation.

    Args:
        lst: A range object to iterate over or None
    """
    total = len(lst)

    min_delta = max(1, int(total**0.5))

    next_update = 1

    for i, elem in enumerate(lst):
        current = i + 1

        should_update = (current >= next_update) or (current == total)

        if should_update:
            percent = (current / total) * 100

            terminal_width = 71
            reserved_space = len(f"{percent:3.0f}%|| {current}/{total}") + 2
            bar_length = max(20, terminal_width - reserved_space)

            filled_length = int(bar_length * current // total)

            if current == total:
                bar = "█" * bar_length
            else:
                bar = "█" * filled_length + " " * \
                    (bar_length - filled_length - 1)

            progress_line = f"\r{percent:3.0f}%|{bar}| {current}/{total}"

            print(progress_line, end="", flush=True)
            next_update = current + min_delta

        yield elem

    print()
