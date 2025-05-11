def plot_segments(canvas, df, n_segments):
    canvas.figure.clf()
    total_len = len(df)
    segment_len = total_len // n_segments

    for i in range(n_segments):
        ax = canvas.figure.add_subplot(n_segments, 1, i + 1)
        start = i * segment_len
        end = (i + 1) * segment_len if i < n_segments - 1 else total_len
        segment = df.iloc[start:end]
        ax.plot(segment['Timestamp'], segment['ADC'])
        ax.set_title(f"Segment {i + 1}")
        ax.tick_params(axis='x', rotation=45)

    canvas.draw()